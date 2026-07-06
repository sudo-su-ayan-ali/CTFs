# Penetration Test Report

## Executive Summary
A successful local privilege escalation was achieved against a vulnerable Ubuntu 18.04.4 LTS host. The target was found to be susceptible to CVE-2023-32629, an OverlayFS-related vulnerability that allowed an unprivileged user to obtain root access and retrieve the root flag.

## Scope
- Target Operating System: Ubuntu 18.04.4 LTS
- Vulnerability: CVE-2023-32629
- Attack Vector: Local privilege escalation
- User Context: Unprivileged shell access

## Assessment Details
The assessment focused on validating whether a low-privileged local user could escalate to root through a known kernel and filesystem vulnerability. The exploitation attempt was executed successfully, demonstrating that the host was vulnerable to the identified issue.

## Findings
### Finding 1: Local Privilege Escalation via OverlayFS
The target system was vulnerable to a local privilege escalation vector involving OverlayFS capability handling. An unprivileged user was able to execute a crafted exploit that resulted in a root shell.

### Impact
Successful exploitation would allow an attacker with limited local access to:
- Gain full root privileges
- Access sensitive files and configuration data
- Read protected content such as root-owned flags and credentials

## Proof of Compromise
The following steps were performed:

1. Created and compiled a local exploit using a publicly known proof-of-concept.
2. Executed the compiled binary from an unprivileged user context.
3. Observed a root shell and successfully accessed the root directory.
4. Retrieved the flag from /root/flag.txt.

### Evidence
```bash
overlay@overlayfs:~$ gcc exp.c
overlay@overlayfs:~$ ./a.out
bash-4.4# id
uid=0(root) gid=0(root)
bash-4.4# cat /root/flag.txt
thm{27aaa5865a52dcd4cb04c0e0a2d39404}
```

## Recommended Remediation
- Apply the latest security updates and patch the vulnerable kernel or operating system.
- Upgrade to a version of Ubuntu with the relevant fix for CVE-2023-32629.
- Restrict local user access and minimize unnecessary privileges where possible.
- Monitor for suspicious mount and namespace activity on affected systems.

## Conclusion
The host was confirmed to be vulnerable to a local privilege escalation condition that allowed an unprivileged user to obtain root access. This issue should be treated as critical from a security perspective and remediated immediately.


