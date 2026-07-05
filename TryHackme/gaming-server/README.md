# Penetration Test Report

## Target
- Host: 10.10.11.245
- Environment: TryHackMe - Gaming Server
- Assessment Type: Authorized security evaluation

## Executive Summary
This assessment demonstrated a complete compromise path from initial reconnaissance to privileged access. The target exposed several weaknesses that enabled unauthorized access to both user-level and root-level data. The most significant issues included exposed sensitive files, weak SSH key protection, and permissive LXD privileges that allowed privilege escalation.

## Scope
The evaluation focused on the following areas:
- Network service discovery
- Web directory enumeration
- SSH key analysis and credential reuse
- Local privilege escalation via LXD

## Methodology
1. Performed host discovery and service enumeration using Nmap.
2. Enumerated web endpoints and directories with Dirb.
3. Reviewed exposed files and recovered an SSH private key.
4. Cracked the key passphrase using a provided wordlist.
5. Leveraged LXD group membership for container-based privilege escalation.

## Findings
### 1. Exposed Sensitive Files on Web Server
The web server exposed directories that contained downloadable artifacts, including a dictionary list and an SSH private key. These materials significantly reduced the effort required to access the target system.

- Severity: High
- Impact: Enabled credential discovery and unauthorized SSH access

### 2. SSH Private Key Protected by Weak Passphrase
A private SSH key was recovered from the web server and its passphrase was cracked using the exposed wordlist. This granted direct access to the user account.

- Severity: High
- Impact: Allowed unauthorized authentication as the user john

### 3. Privilege Escalation via LXD
The compromised user belonged to the lxd group, which allowed the creation of a privileged container and mounting of the host filesystem. This path led to root access.

- Severity: Critical
- Impact: Full system compromise was achieved

## Evidence Summary
The assessment produced the following key outcomes:
- User access was obtained via SSH using the recovered private key.
- User flag was recovered successfully.
- Root access was achieved through LXD privilege escalation.
- Root flag was recovered successfully.

## Recommended Remediations
- Remove or restrict access to sensitive files from publicly reachable directories.
- Enforce strong SSH key passphrases and rotate any exposed credentials.
- Remove the lxd group from non-administrative users.
- Disable privileged container creation for untrusted users.
- Apply least-privilege principles to service accounts and user roles.

## Conclusion
The target was successfully compromised through a chain of misconfigurations and weak access controls. The primary weaknesses were the exposure of sensitive artifacts, insufficient protection of SSH credentials, and overly permissive privilege escalation paths. These issues should be addressed immediately to reduce the risk of unauthorized access.

## Notes
This report documents a controlled security assessment performed in a training environment. The findings are intended for educational and defensive improvement purposes.
