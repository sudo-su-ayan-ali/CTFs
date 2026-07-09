# Penetration Test Report

## Target Environment
- Target Host: 10.48.140.133
- Assessment Type: Authorized security assessment in a controlled lab environment
- Platform: Linux-based host within the TryHackMe Fowsniff CTF scenario
- Date: 2026-07-09

## Executive Summary
This assessment evaluated the security posture of the target host through host discovery, service enumeration, credential analysis, and limited post-exploitation testing. The environment exhibited several weaknesses that significantly reduced the effectiveness of its defensive controls. The most critical issues involved exposed authentication services, weak credential handling, and the use of insecure password storage practices.

The findings demonstrate that unauthorized access could be achieved through a combination of weak credentials, publicly accessible services, and poor password hygiene. These conditions materially increased the risk of account compromise and further system access.

## Scope and Objectives
The assessment focused on:
- Enumeration of exposed services and open ports
- Review of web and network-facing services
- Evaluation of authentication controls for SSH and POP3
- Analysis of password strength and credential reuse
- Identification of potential post-exploitation paths

## Methodology
The review followed a structured workflow:
1. Passive and active reconnaissance to identify reachable services
2. Service fingerprinting and version identification using Nmap
3. Authentication testing against exposed services
4. Offline cracking of recovered password hashes
5. Assessment of privilege escalation and persistence opportunities

## Summary of Findings
| Severity | Finding | Impact |
|---|---|---|
| High | Weak credentials and password reuse were present across services | Enabled account compromise and unauthorized access |
| High | POP3 access was available with recovered credentials | Exposed mailbox content and sensitive communications |
| High | SSH authentication relied on weak or easily recoverable credentials | Allowed direct system access |
| Medium | Permission misconfigurations and writable service components increased escalation risk | Amplified the impact of initial compromise |

## Detailed Findings

### 1. Weak Credential Exposure
Recovered credential material showed that several accounts used weak passwords that were susceptible to offline cracking. The use of unsalted MD5 hashes further reduced the resistance of the stored credentials against attack.

Impact:
- Unauthorized access to multiple accounts
- Increased risk of lateral movement and reuse across services

### 2. POP3 Service Exposure
The POP3 service was reachable and accepted authentication when valid credentials were supplied. This exposed mail content that could contain sensitive personal or organizational information.

Impact:
- Confidential data disclosure
- Increased risk of phishing, impersonation, or further compromise

### 3. SSH Authentication Weaknesses
Weak SSH credentials were identified and successfully used to access the target system. This demonstrates that remote authentication controls were insufficiently hardened.

Impact:
- Remote shell access to the host
- Greater opportunity for persistence and privilege escalation

### 4. Post-Exploitation Opportunities
The environment also revealed opportunities for further compromise through weak file permissions and writable execution paths. These conditions increased the potential impact of a successful foothold.

Impact:
- Elevated privileges or persistence potential
- Greater operational impact following initial compromise

## Evidence Collected
The following services were identified during enumeration:
- TCP/22 - SSH
- TCP/80 - HTTP
- TCP/110 - POP3
- TCP/143 - IMAP

The host was confirmed to run:
- OpenSSH 7.2p2
- Apache httpd 2.4.18
- Dovecot POP3/IMAP services

## Recommended Remediation
The following actions are recommended to strengthen the environment:
- Enforce strong password policies and prohibit password reuse across systems
- Replace MD5-based password storage with modern password hashing algorithms such as bcrypt, scrypt, or Argon2
- Disable unnecessary POP3 access or require encrypted transport where it is needed
- Rotate all exposed credentials immediately
- Enforce key-based SSH authentication and restrict access to authorized users only
- Review file and directory permissions to eliminate writable paths that may enable privilege escalation

## Conclusion
The target system demonstrated several common but serious security weaknesses, including weak authentication practices, insecure password storage, and overly permissive service exposure. These issues created a practical path to unauthorized access and increased the potential impact of compromise. Stronger credential management, modern hashing schemes, and tighter access controls are essential to reduce the identified risks.

## Notes
This report reflects a controlled CTF-style assessment environment and is intended for educational and defensive analysis purposes.
