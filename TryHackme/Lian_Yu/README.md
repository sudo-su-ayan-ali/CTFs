# Penetration Test Report: Lian_Yu System Assessment

**Date of Assessment:** July 22, 2026

**Assessment Type:** Infrastructure & Web Application Penetration Test

**Target IP:** 10.10.70.37

## 1. Executive Summary

A comprehensive penetration test was conducted against the Lian_Yu server to evaluate its security posture. The assessment simulated an unauthenticated, external attacker aiming to identify vulnerabilities, gain unauthorized access, and escalate privileges to the administrative (root) level.

The engagement revealed several critical security flaws, including insecure storage of sensitive information, weak cryptographic implementations, weak credential policies, and misconfigured system binaries. By chaining these vulnerabilities, complete systemic compromise was achieved.

### 1.1 Key Findings Summary

|**Risk Level**|**Vulnerability**|**Description**|
|---|---|---|
|**Critical**|**Insecure Sudo Configuration**|Misconfigured `sudo` permissions allowed execution of `pkexec`, leading to immediate root privilege escalation.|
|**High**|**Cleartext Credential Storage**|SSH credentials were hidden within an image file using weak steganography and a common password.|
|**Medium**|**Information Disclosure**|Hidden web directories and source code comments leaked valid usernames and encoded passwords.|

## 2. Assessment Methodology & Attack Narrative

The assessment followed a standard penetration testing methodology: Reconnaissance, Enumeration, Exploitation, and Privilege Escalation.

### 2.1 Reconnaissance & Port Scanning

An initial TCP port scan was conducted using `nmap` to identify exposed services. The target was identified as a Debian-based Linux system.

**Open Services:**

- **Port 21/TCP:** FTP (vsftpd 3.0.2)
    
- **Port 22/TCP:** SSH (OpenSSH 6.7p1)
    
- **Port 80/TCP:** HTTP (Apache httpd)
    
- **Port 111/TCP:** RPCBind
    

### 2.2 Web Enumeration & Information Disclosure

Manual interaction and automated directory brute-forcing (using `gobuster`) against the web service on Port 80 revealed hidden directories and files.

1. **Directory Discovery:** A nested directory structure (`/island/2100/`) was discovered.
    
2. **Token Leakage:** Brute-forcing files with a `.ticket` extension within `/2100/` revealed a file named `green_arrow.ticket`.
    
3. **Cryptographic Weakness:** The `.ticket` file contained a Base58 encoded string: `RTy8yhBQdscX`. Upon decoding, this yielded a plaintext password: `!#th3h00d`.
    
4. **Source Code Leakage:** Reviewing the page source of the `/island` endpoint revealed a hidden HTML comment containing a potential username: `vigilante`.
    

### 2.3 Initial Access (FTP) & Steganography

The discovered credentials (`vigilante` / `!#th3h00d`) were utilized to authenticate against the FTP service on Port 21.

Three image files were recovered from the user's home directory. Analysis of the image `aa.jpg` revealed embedded steganographic data.

- A dictionary attack using `stegcracker` and a standard wordlist (`rockyou.txt`) successfully bypassed the passphrase, which was set to the weak string `password`.
    
- The extracted archive contained a file named `shado`, which held an additional credential string: `M3tahuman`.
    

### 2.4 Internal Access (SSH)

The newly discovered credential (`M3tahuman`) was tested against the SSH service. The system allowed authentication for the user `slade`.

- **Proof of Concept (User Compromise):** Read access to `/home/slade/user.txt` was achieved.
    

### 2.5 Privilege Escalation

Upon gaining a local shell session, internal system enumeration was conducted to identify privilege escalation vectors.

Reviewing the `sudo` privileges for the user `slade` (`sudo -l`) revealed an insecure configuration. The user was permitted to execute `/usr/bin/pkexec` as the root user without restrictions on target binaries.

**Exploitation:**

By invoking `pkexec` via `sudo`, arbitrary commands could be executed with root privileges.

- **Command Executed:** `sudo pkexec cat /root/root.txt`
    
- **Proof of Concept (System Compromise):** Full read access to the root directory was verified, confirming total system compromise.
    

## 3. Remediation & Recommendations

To secure the Lian_Yu system against the attack vectors utilized during this assessment, the following remediation steps are strongly recommended:

1. **Audit and Restrict Sudoers Configuration (Critical):** Remove the entry allowing the user `slade` to run `pkexec` via `sudo`. If specific administrative tasks are required for this user, follow the principle of least privilege and restrict execution strictly to the necessary binaries.
    
2. **Enforce Strong Password Policies (High):** Do not rely on weak passwords (e.g., `password`) for securing sensitive files or archives. Implement and enforce a robust password policy across all services.
    
3. **Sanitize Web Directories (Medium):** Remove sensitive configuration files, "tickets," and encoded credentials from web-accessible directories. Web servers should strictly serve application files and static assets.
    
4. **Remove Developer Comments (Low):** Strip all developer comments containing sensitive information (such as internal usernames or internal application logic) from the HTML source code prior to production deployment.
