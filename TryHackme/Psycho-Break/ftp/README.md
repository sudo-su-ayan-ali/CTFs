# Penetration Testing Report

## Assessment Summary

This report documents a controlled penetration test of the TryHackMe room "Psycho Break". The objective was to assess the target host across exposed services, web application components, encoded artifacts, and privilege escalation paths. The assessment was completed successfully and resulted in both user-level and root-level access within the lab environment.

## Scope

- Target host: 10.10.172.137
- Operating system: Ubuntu Linux
- Services assessed: FTP, SSH, and HTTP
- Objective: Demonstrate practical offensive tradecraft in a contained CTF environment

## Executive Summary

The target environment exposed multiple attack surfaces that provided a realistic path for reconnaissance and compromise. Initial enumeration identified open network services and a web application with hidden content and challenge-based clues. Subsequent analysis of artifacts, credential material, and a supplied binary enabled access to the user account, while abuse of a scheduled task revealed a privilege escalation vector leading to root-level compromise.

## Methodology

1. Network reconnaissance and service discovery
2. Port scanning and service fingerprinting
3. Web enumeration and directory discovery
4. Analysis of encoded clues and file artifacts
5. Credential analysis and binary inspection
6. Privilege escalation through scheduled task abuse
7. Validation of user and root compromise

## Findings

### 1. Network Exposure

A full TCP scan identified three open services:

- 21/tcp — ProFTPD 1.3.5a
- 22/tcp — OpenSSH 7.2p2
- 80/tcp — Apache HTTP Server 2.4.18

The exposure of FTP, SSH, and web services created multiple initial footholds for continued evaluation.

### 2. Web Application Enumeration

The web application exposed several embedded clues and hidden paths. Directory enumeration and manual inspection revealed key artifacts that were necessary to progress through the challenge. These findings demonstrate the value of structured reconnaissance and content discovery in identifying hidden functionality.

### 3. Credential and Artifact Recovery

The assessment successfully recovered the following challenge-related credentials and clues:

- FTP username: joseph
- FTP password: intotheterror445
- Map access key: Grant_me_access_to_the_map_please
- Keeper key: 48ee41458eb0b43bf82b986cecf3af01
- Binary challenge key: kidman

### 4. Binary Analysis

A supplied binary was inspected to recover a hidden passphrase. Analysis of the program output revealed the following decoded value:

- KIDMANSPASSWORDISSOSTRANGE

This step highlights the importance of reverse engineering and logic-based analysis when evaluating binary artifacts.

### 5. Privilege Escalation

A root-owned cron task was identified and abused to execute arbitrary commands with elevated privileges. This represented a clear privilege escalation path and enabled access to the root flag within the lab environment.

## Evidence Collected

- User flag: 4C72A4EF8E6FED69C72B4D58431C4254
- Root flag: BA33BDF5B8A3BFC431322F7D13F3361E

## Risk Assessment

The target environment demonstrated several common weaknesses associated with intentionally vulnerable systems, including excessive service exposure, weak credential handling, and poor privilege separation for scheduled tasks. Though the target was a controlled CTF scenario, these issues are representative of patterns often seen in real-world systems.

## Recommendations

- Restrict exposure of administrative and file transfer services to approved networks.
- Enforce strong credentials and rotate them regularly.
- Review scheduled tasks and remove unnecessary privileged automation.
- Apply least-privilege principles to service accounts and automation scripts.
- Continue testing web application traversal controls and hidden content exposure.

## Conclusion

The assessment was successfully completed through a multi-stage attack chain spanning reconnaissance, web enumeration, artifact recovery, binary analysis, and privilege escalation. The exercise demonstrated realistic adversarial tradecraft and reinforced the need for layered defensive controls.
