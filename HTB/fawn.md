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

![FTP Help](
<img width="499" height="169" alt="Screenshot_20250726_132850" src="https://github.com/user-attachments/assets/9bf61b9b-adec-4e68-8d3d-5b3dc74db496" />
<img width="502" height="124" alt="Screenshot_20250726_132902" src="https://github.com/user-attachments/assets/fd54b8c5-7d15-4b35-85d2-897b76e1f38e" />
)

List files in the directory:

![FTP List](
<img width="735" height="524" alt="Screenshot_20250726_132918" src="https://github.com/user-attachments/assets/e783ae27-3ca2-4d6a-909b-f7136a148849" />
)


---

## Getting the Flag

Download the `flag.txt` file:

![FTP Get Flag](
<img width="731" height="157" alt="Screenshot_20250726_132936" src="https://github.com/user-attachments/assets/ee6e9b89-83d2-4067-95ee-8a59056a0b39" />

)

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

![Flag Reveal](<img width="425" height="209" alt="Screenshot_20250726_133006" src="https://github.com/user-attachments/assets/f522e995-4ce7-49dc-aa0f-511819190236" />
)

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
