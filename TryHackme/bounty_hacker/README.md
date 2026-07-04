# Bounty Hacker – Professional Report

## Executive Summary
This report documents the successful compromise of the TryHackMe room "Bounty Hacker". The objective was to gain initial access to the target system, retrieve the user flag, escalate privileges, and obtain the root flag. The assessment was completed through reconnaissance, anonymous FTP access, SSH credential cracking, and a sudo privilege escalation.

## 1. Objectives
The goals of this engagement were to:
- Identify exposed services and potential entry points.
- Obtain initial access to the target machine.
- Recover the user flag.
- Escalate privileges to root.
- Retrieve the root flag.

## 2. Reconnaissance and Enumeration
A network enumeration scan revealed three services exposed on the target host:
- FTP on port 21: vsftpd 3.0.5
- SSH on port 22: OpenSSH 8.2p1
- HTTP on port 80: Apache 2.4.41

The most significant observation was that anonymous FTP login was enabled, which provided a viable path for initial access.

## 3. Initial Access
### 3.1 FTP Enumeration
The target allowed anonymous authentication over FTP. After connecting to the service, two files were discovered:
- task.txt
- locks.txt

The file task.txt contained a clue suggesting the username involved in the later SSH attack:
- Protect Vicious.
- Plan for Red Eye pickup on the moon.
- -lin

The file locks.txt contained a list of candidate passwords, which was used as a password dictionary for further attacks.

### 3.2 Credential Cracking
Hydra was used to test the discovered password list against the SSH service for the username lin. The attack successfully identified the password:
- RedDr4gonSynd1cat3

## 4. Foothold and User Flag
SSH access was successfully established as the user lin using the recovered password. Once authenticated, the user flag was retrieved from the Desktop directory:
- User flag: THM{CR1M3_SyNd1C4T3}

## 5. Privilege Escalation
A review of the current user's sudo permissions showed that lin could execute tar as root:
- (root) /bin/tar

This misconfiguration was exploited using a well-known tar privilege escalation technique. A root shell was spawned by running:

```bash
sudo tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

With root privileges obtained, the root flag was recovered:
- Root flag: THM{80UN7Y_h4cK3r}

## 6. Findings and Conclusion
The target was successfully compromised through a combination of:
- Service enumeration.
- Anonymous FTP access.
- SSH password cracking.
- Sudo misconfiguration abuse for privilege escalation.

This exercise demonstrates the importance of disabling anonymous access where unnecessary, enforcing strong authentication, and restricting sudo privileges to only what is required.

## 7. Summary of Key Outcomes
- Initial access was achieved through anonymous FTP.
- SSH credentials for lin were recovered and validated.
- The user flag was obtained.
- Privilege escalation to root was achieved through sudo access to tar.
- The root flag was retrieved successfully.
