# CTF Report

**Target:** 10.129.17.147  
**Date:** 2025-08-03  
**Tester:** Ayan Ali

---

## 1. Executive Summary

During a targeted penetration test of the host at `10.129.17.147`, a critical vulnerability was discovered in the web application running on port 80. The login functionality was found to be susceptible to SQL Injection, allowing unauthorized access to the application and exposure of sensitive information.

---

## 2. Methodology

### 2.1 Reconnaissance

- **Tool Used:** Nmap
- **Command:**
    
    text
    
    ```
    sudo nmap -Pn 10.129.17.147 -vv
    ```
    
- **Findings:**
    - Host is up.
    - Port 80/tcp (HTTP) is open.

### 2.2 Enumeration

- Navigated to `http://10.129.17.147` in a web browser.
- Observed a login page requiring username and password.

### 2.3 Exploitation

#### 2.3.1 SQL Injection

- **Attack Vector:**
    - Username: `admin'#`
    - Password: `asdf`
- **Result:**
    - Successfully bypassed authentication.
    - Gained unauthorized access to the application.
    - Retrieved the following flag:
        
        text
        
        ```
        e3d0796d002a446c0e622226f42e9672
        ```
        

---

## 3. Vulnerability Details

### 3.1 SQL Injection in Login Form

- **Description:**  
    The login form does not properly sanitize user input, allowing attackers to manipulate the SQL query and bypass authentication.
- **Payload Used:**
    - Username: `admin'#`
    - Password: `asdf`
- **Impact:**
    - Unauthorized access to the application.
    - Potential exposure of sensitive data.

---

## 4. Recommendations

- **Implement input validation and parameterized queries** to prevent SQL injection.
- **Sanitize all user-supplied input** before processing.
- **Conduct regular security assessments** of web applications.

---

## 5. Conclusion

A critical SQL Injection vulnerability was identified in the login functionality of the web application on `10.129.17.147`. Immediate remediation is recommended to prevent unauthorized access and potential data breaches.

---

**Flag Obtained:**

text

```
e3d0796d002a446c0e622226f42e9672
```

---

_Report prepared by: Ayan Ali_  
_Date: 2025-08-03_
