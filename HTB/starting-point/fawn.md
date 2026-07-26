# HTB: Fawn Walkthrough

## Table of Contents

- Enumeration
- FTP Access
- FTP Commands
- Getting the Flag
- Flag Submission

---

## Enumeration

First, we scan the target with `nmap` to identify open ports and services.

Bash

```
nmap -Pn -sV -sC -vv 10.129.216.196 -oN nmap.txt
```

**Key Findings:**

- **Port 21/tcp** is open and running **vsftpd 3.0.3**
- **Anonymous FTP login is allowed**
- A file named `flag.txt` is present

<details> <summary>Click to expand nmap output</summary>

text

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0               32 Jun 04  2021 flag.txt
Service Info: OS: Unix
```

</details>

---

## FTP Access

Connect to the FTP server using anonymous login:

![FTP Login](https://lmarena.ai/c/Screenshot_20250726_132850.png)

Bash

```
ftp {target_IP}
# Name: anonymous
# Password: anon123
```

Successful login:

![FTP Login Success](https://lmarena.ai/c/Screenshot_20250726_132902.png)

---

## FTP Commands

You can use `help` to list available FTP commands:

![FTP Help](https://lmarena.ai/c/Screenshot_20250726_132918.png)

List files in the directory:

![FTP List](https://lmarena.ai/c/Screenshot_20250726_132936.png)

---

## Getting the Flag

Download the `flag.txt` file:

![FTP Get Flag](https://lmarena.ai/c/Screenshot_20250726_132955.png)

ftp

```
get flag.txt
```

Exit the FTP session:

ftp

```
bye
```

---

## Flag Submission

Check the contents of `flag.txt`:

![Flag Reveal](https://lmarena.ai/c/Screenshot_20250726_133006.png)

Bash

```
cat flag.txt
# 035db21c881520061c53e0536e44f815
```

---

## Summary

- Enumerated open ports and found FTP with anonymous access
- Logged in and downloaded the flag
- Retrieved the flag for submission

---

**Flag:**

text

```
035db21c881520061c53e0536e44f815
```

---

> _Happy Hacking!_

---

**Note:**  
Replace `{target_IP}` with your actual target IP address.  
All screenshots are referenced as `./Screenshot_*.png` — adjust paths as needed for your repo.
