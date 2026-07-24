# Penetration Testing Assessment Report

**Target:** `Blaster` (TryHackMe Practice Environment)

**Assessment Type:** Infrastructure & Web Application Security Assessment

**Severity Summary:** Critical

---

## 1. Executive Summary

An assessment was performed against the target host **Blaster** to identify security vulnerabilities, evaluate potential exploitation paths, and assess the overall risk to the host environment.

During testing, multiple critical vulnerabilities were identified that allowed an attacker to transition from initial unauthenticated reconnaissance to full system compromise (**`NT AUTHORITY\SYSTEM`**).

* **Initial Access:** Unauthenticated web directory enumeration revealed exposed credentials embedded within a publicly accessible web page.
* **Remote Access:** Exposed Remote Desktop Protocol (RDP) on standard port 3389 allowed credential-based login to a low-privileged user account.
* **Privilege Escalation:** A vulnerability in executable privilege elevation combined with misconfigured User Account Control (UAC) permitted arbitrary execution of an elevated command shell, granting administrative rights.

---

## 2. Assessment Findings & Technical Breakdown

### Finding 1: Sensitive Information Disclosure via Public Web Directory

* **Severity:** High
* **Vector:** HTTP (Port 80)
* **Description:** Direct forced browsing and directory enumeration uncovered hidden web paths containing hardcoded user credentials within web page content and comments.
* **Impact:** Allows unauthorized external actors to obtain valid system credentials without brute-force attempts.
* **Remediation:** Remove hardcoded credentials, sensitive developer notes, or debugging artifacts from public-facing web applications. Implement strict access controls on web directories.

---

### Finding 2: Exposed Remote Desktop Protocol (RDP) Service

* **Severity:** Medium
* **Vector:** RDP (Port 3389)
* **Description:** The RDP service was directly exposed to the network without additional network-level security controls (e.g., VPN or IP whitelisting).
* **Impact:** Combined with leaked or weak credentials, exposed remote management interfaces allow attackers direct interactive GUI/CLI access to the internal system.
* **Remediation:** Restrict management interfaces (RDP, SSH, WinRM) behind a secure VPN gateway or jump box. Enforce Network Level Authentication (NLA) and multi-factor authentication (MFA).

---

### Finding 3: Local Privilege Escalation via Windows Binary / UAC Bypass

* **Severity:** Critical
* **Vector:** Local Executable Execution / Windows PrivEsc
* **Description:** Once local access was established, the user environment allowed running specific legacy/vulnerable executables capable of launching sub-processes (such as Internet Explorer or HH.exe) with elevated privileges, effectively bypassing local UAC controls to spawn an interactive `cmd.exe` shell as `SYSTEM`.
* **Impact:** Full compromise of host confidentiality, integrity, and availability. An attacker achieves complete control over local user accounts, file systems, and system configurations.
* **Remediation:**
* Enforce the Principle of Least Privilege across all local accounts.
* Apply vendor security patches and ensure OS binaries/components are kept up to date.
* Restrict local administrators from running unverified binaries or legacy utilities capable of spawning elevated sub-processes.



---

## 3. Remediation Roadmap

[ Immediate Actions ]
├── Remove plain-text credentials from web server directories
└── Implement Multi-Factor Authentication (MFA) for RDP access

[ Short-Term Fixes ]
├── Restrict RDP exposure behind a secure VPN / Bastion Host
└── Audit user group permissions and local administrator rights

[ Long-Term Controls ]
├── Implement Endpoint Detection & Response (EDR) for anomalous process creation
└── Establish routine vulnerability management & patch deployment cycles


