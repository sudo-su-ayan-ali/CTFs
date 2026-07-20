# Penetration Test Report: Target 10.49.165.155

## 1. Executive Summary

During the security assessment of target IP **10.49.165.155**, multiple critical vulnerabilities were discovered that allowed for complete system compromise. The attack chain leveraged weak credentials on a WebDAV directory to achieve Initial Access, followed by exploiting a misconfigured `sudo` permission to achieve Privilege Escalation. Full administrative (`root`) control over the server was successfully established.

**Overall Risk Rating:** **CRITICAL**

## 2. Attack Narrative & Kill Chain

The following section details the step-by-step methodology used to compromise the target system.

### Phase 1: Reconnaissance & Enumeration

An initial port scan using `nmap` identified a web server running on the target.

- **Port 80 (TCP):** Running Apache httpd 2.4.18 (Ubuntu).
    

Directory brute-forcing with `dirsearch` revealed several hidden files and a protected directory:

- `/webdav/` returned a **401 Unauthorized** response, indicating a protected WebDAV endpoint.
    

### Phase 2: Vulnerability Discovery & Initial Access

Using `davtest`, the `/webdav/` directory was probed for default/weak credentials and file upload permissions.

- **Authentication Bypass:** Access was successfully granted using the weak credential pair `wampp:xampp`.
    
- **File Upload/Execution:** The directory permitted the upload and execution of multiple file types, most notably `.php` and `.txt` files.
    

An attacker payload (`php-reverse-shell.php`) was manually uploaded to the server utilizing the `cadaver` WebDAV client. Upon navigating to the uploaded payload via the web browser, a reverse shell connection was established to the listening Netcat on the attack machine (port 1234).

**Result:** Initial access achieved as the `www-data` user.

### Phase 3: Post-Exploitation & Privilege Escalation

Upon gaining a foothold as `www-data`, local enumeration was conducted to identify privilege escalation vectors.

Checking the user's `sudo` privileges (`sudo -l`) revealed a severe misconfiguration:

- **Rule:** `(ALL) NOPASSWD: /bin/cat`
    
- **Impact:** The `www-data` user is permitted to read any file on the system as `root` without requiring a password.
    

This vulnerability was immediately leveraged to read sensitive system files, culminating in the extraction of the root flag, confirming total system compromise.

## 3. Proof of Compromise (Flags)

|**Privilege Level**|**Location**|**Flag Hash**|
|---|---|---|
|**User** (`www-data`)|`/home/merlin/user.txt`|`449b40fe93f78a938523b7e4dcd66d2a`|
|**Root** (`root`)|`/root/root.txt`|`101101ddc16b0cdf65ba0b8a7af7afa5`|

## 4. Technical Findings & Remediation

### Finding 1: Weak/Default Credentials on WebDAV

**Severity:** **CRITICAL**

- **Description:** The WebDAV directory `/webdav` is protected by basic authentication but utilizes highly guessable, default credentials (`wampp:xampp`).
    
- **Remediation:** Enforce a strong password policy. Ensure default vendor credentials are changed immediately upon deployment. Consider implementing multi-factor authentication or restricting access to the `/webdav` endpoint to trusted internal IP addresses only.
    

### Finding 2: Unrestricted File Upload Leading to RCE

**Severity:** **CRITICAL**

- **Description:** The WebDAV configuration does not restrict the types of files that can be uploaded or executed. This allowed the upload of a malicious `.php` script, which the Apache server executed, leading to Remote Code Execution (RCE).
    
- **Remediation:** Disable the execution of server-side scripts (like PHP) within the WebDAV directory. This can be done in Apache by disabling the PHP engine for that specific directory block (e.g., `php_admin_flag engine off`). Restrict upload permissions to only strictly necessary file extensions.
    

### Finding 3: Insecure Sudo Configuration (Privilege Escalation)

**Severity:** **HIGH**

- **Description:** The `www-data` service account is authorized to execute `/bin/cat` as `root` without a password. While `cat` is generally used to read files, running it as root allows a low-privileged web user to read sensitive files such as `/etc/shadow` (password hashes), SSH keys, or application configuration files containing database credentials.
    
- **Remediation:** Remove the `NOPASSWD: /bin/cat` entry from the `/etc/sudoers` file. Service accounts like `www-data` should operate with the principle of least privilege and should rarely, if ever, require `sudo` access.
