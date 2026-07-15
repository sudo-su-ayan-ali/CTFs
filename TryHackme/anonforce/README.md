# Penetration Testing Report: Anonforce (TryHackMe)

## 1. Executive Summary

During a routine security assessment of the **Anonforce** environment, a critical vulnerability chain was identified that allowed for full system compromise. An insecurely configured FTP service permitted anonymous access, exposing sensitive cryptographic keys. By leveraging these keys and utilizing offline brute-force attacks against system password hashes, root-level administrative access was successfully achieved via SSH.

## 2. Assessment Summary & Scope

- **Target Machine:** Anonforce (TryHackMe)
    
- **Objective:** Identify vulnerabilities, escalate privileges, and secure root/user flags.
    
- **Severity:** **Critical** (Full Host Compromise)
    

## 3. Attack Chain Timeline

```
[Anonymous FTP Access] ➔ [Exfiltrate PGP Keys] ➔ [Crack PGP Key Passphrase] ➔ [Decrypt /etc/shadow] ➔ [Crack Root Hash] ➔ [Root SSH Access]
```

## 4. Technical Findings & Exploitation Walkthrough

### Phase 1: Reconnaissance & Port Scanning

An initial comprehensive TCP port scan was conducted across all 65,535 ports to identify the target's attack surface.

Bash

```
nmap -p- -T4 -sV $IP
```

**Discoveries:**

- **Port 21/TCP:** FTP (File Transfer Protocol)
    
- **Port 22/TCP:** SSH (Secure Shell)
    

### Phase 2: Vulnerability Exploitation (Information Disclosure via FTP)

The FTP service was found to have **Anonymous Authentication** enabled. A connection was established using the `anonymous` username and a blank password.

Upon reviewing the filesystem structure, a non-standard directory named `/notread` was discovered.

Bash

```
ftp $IP
Name: anonymous
Password: 
ftp> cd notread
ftp> ls -la
```

**Exfiltrated Artifacts:** The directory contained PGP (Pretty Good Privacy) cryptographic artifacts:

- `private.asc`: A PGP private key block (ASCII-armored).
    
- `backup.pgp`: An encrypted backup archive.
    

The files were downloaded locally using `mget *` for offline analysis.

### Phase 3: Cryptanalysis & PGP Decryption

To read the encrypted backup file, the passphrase protecting the `private.asc` key needed to be cracked.

1. **Hash Extraction:** The private key was converted into a format compatible with John the Ripper using `gpg2john`.
    
    Bash
    
    ```
    gpg2john private.asc > private.hash
    ```
    
2. **Offline Passphrase Cracking:** A dictionary attack was launched against the hash utilizing the `rockyou.txt` wordlist.
    
    Bash
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt private.hash
    ```
    
    _Result: The passphrase was successfully recovered within seconds._
    
3. **Data Decryption:** The private key was imported into the local GnuPG keyring, and the backup file was decrypted.
    
    Bash
    
    ```
    gpg --import private.asc
    # (Entered the cracked passphrase when prompted)
    
    gpg --decrypt backup.pgp > decrypted_backup.txt
    ```
    

### Phase 4: Privilege Escalation (Password Cracking)

The decrypted `backup.pgp` file was revealed to be a backup of the target system's `/etc/shadow` file, exposing local user password hashes.

**Identified Accounts:**

- `root`: Utilizing a SHA-512 crypt hash (`$6$`).
    
- `melodias`: Utilizing an MD5 crypt hash (`$1$`).
    

An offline dictionary attack was targeted against these hashes:

Bash

```
john --wordlist=/usr/share/wordlists/rockyou.txt decrypted_backup.txt
```

_Result: The plain-text password for the `root` account was successfully cracked._

### Phase 5: Post-Exploitation & Proof of Possession

Using the recovered plain-text credentials for the `root` user, an interactive SSH session was established, granting full administrative control over the machine.

Bash

```
ssh root@$IP
```

**Flag Retrieval:**

- **Root Flag:** Located at `/root/root.txt`
    
- **User Flag:** Located at `/home/melodias/user.txt`
    

## 5. Remediation Recommendations

|Vulnerability|Impact|Mitigation Strategy|
|---|---|---|
|**Anonymous FTP Access**|High|**Disable anonymous logins** in the FTP configuration file (e.g., `anonymous_enable=NO` in `vsftpd.conf`).|
|**Sensitive Data Exposure**|Critical|**Remove cryptographic keys and system backups** from publicly accessible web/file directories.|
|**Weak Password Policy**|High|Implement strong password complexity requirements and regular rotation policies to mitigate offline dictionary attacks. Enforce the use of **SSH keys** instead of passwords for SSH authentication.|