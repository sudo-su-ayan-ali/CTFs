# Penetration Test Report: The Cod Caper (TryHackMe)

## 1. Executive Summary

This report documents the findings of a penetration test conducted against the target environment, "The Cod Caper" (Pingu's Server). The objective of this engagement was to identify security vulnerabilities, demonstrate their impact through exploitation, and provide actionable remediation guidance.

During the assessment, critical vulnerabilities were discovered that allowed for full system compromise. The attack chain began with a web-based **SQL Injection (SQLi)** vulnerability, which provided administrative web credentials. This access was leveraged to achieve initial remote command execution. Following local system enumeration, a custom binary was found to be vulnerable to a **Stack-Based Buffer Overflow**, which was subsequently exploited to escalate privileges to `root`.

## 2. Assessment Methodology

The engagement followed standard penetration testing methodologies, closely aligning with the Offensive Security framework. The phases included:

1. **Information Gathering:** Port scanning and service fingerprinting to identify the attack surface.
    
2. **Vulnerability Assessment & Web Enumeration:** Discovering hidden directories and testing web inputs for injection flaws.
    
3. **Exploitation:** Weaponizing the discovered SQLi to extract credentials and achieve a foothold via a reverse shell.
    
4. **Privilege Escalation:** Conducting internal enumeration and utilizing reverse engineering (GDB/pwndbg) to develop a custom memory corruption exploit.
    

## 3. Detailed Attack Narrative

### 3.1 Reconnaissance and Enumeration

The assessment began with a full TCP port scan using `nmap`. The scan revealed two open ports:

- **Port 22 / TCP:** SSH service
    
- **Port 80 / TCP:** Apache HTTP web server
    

With the web server identified as the primary target, directory brute-forcing was initiated using `gobuster`. This enumeration revealed hidden administrative login portals that were previously unlinked from the main application flow.

### 3.2 Initial Access (Web Exploitation)

Manual interaction with the discovered administrative login form revealed a lack of input sanitization. The login form was tested using `sqlmap`, which confirmed it was highly vulnerable to **SQL Injection**.

By exploiting the database through the vulnerable POST parameters, the database was dumped, yielding the administrator's plaintext credentials. Logging into the administrative portal with these credentials exposed a command execution feature. A `netcat` (nc) reverse shell payload was crafted and executed, granting initial low-privileged access to the underlying Linux system as the user `pingu`. Additional enumeration using the `find` command located the user's hidden SSH password, establishing persistence.

### 3.3 Privilege Escalation

Once local access was secured, `LinEnum.sh` was transferred to the target to identify privilege escalation vectors. The script highlighted a custom binary running with **SUID (Set Owner User ID) permissions**, meaning it executed with the privileges of its owner: `root`.

The binary was downloaded to the attacker machine and analyzed using `gdb` with the `pwndbg` extension. Dynamic analysis revealed that the binary did not properly validate input length, making it vulnerable to a **Stack-Based Buffer Overflow**.

By calculating the exact offset to overwrite the Instruction Pointer (EIP/RIP), a custom exploit was developed. The exploit was successfully delivered using two methods:

1. **Manual Execution:** Passing a crafted payload utilizing proper Little Endian formatting.
    
2. **Scripted Execution:** Utilizing Python's `pwntools` library to automate the payload delivery.
    

Execution of the buffer overflow payload hijacked the binary's control flow, spawning a root shell and resulting in a complete compromise of the machine.

## 4. Vulnerability Findings & Remediation

### Finding 1: Unauthenticated SQL Injection (SQLi)

- **Severity:** **Critical**
    
- **Description:** The administrative login form dynamically concatenates user input directly into SQL queries without proper sanitization or parameterization. This allowed an unauthenticated attacker to bypass authentication and dump the database.
    
- **Remediation:** Implement **Prepared Statements** (Parameterized Queries) within the application's backend code. Avoid using dynamic SQL queries. Ensure all user input is strictly validated and sanitized before processing.
    

### Finding 2: Insecure Web Application Architecture (Command Execution)

- **Severity:** **High**
    
- **Description:** The administrative portal contains functionality that allows authenticated users to execute arbitrary system commands. Because this web application runs in the context of a system user, this directly led to a remote shell.
    
- **Remediation:** Remove web-based command execution functionality. If administrative tasks are required, implement strict, hardcoded scripts that do not accept arbitrary string inputs from the web interface.
    

### Finding 3: Buffer Overflow in SUID Binary

- **Severity:** **Critical**
    
- **Description:** A custom binary on the system lacked bounds checking on user input (e.g., using unsafe functions like `strcpy` or `gets`). Because the SUID bit was set on this file, exploiting the memory corruption flaw yielded a root shell.
    
- **Remediation:**
    
    1. **Code Level:** Rewrite the binary using safe memory functions (e.g., `strncpy`, `fgets`) that enforce strict input length limits.
        
    2. **System Level:** Remove the SUID bit from the binary if it is not strictly required for system operation (`chmod u-s <binary>`).
        
    3. **Compiler Defenses:** Recompile the binary utilizing modern exploit mitigations such as Stack Canaries, NX (No-eXecute), and ASLR/PIE (Position Independent Executable).
