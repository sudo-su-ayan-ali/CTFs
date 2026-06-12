# TryHackMe / Cyborg

## Summary

This write-up documents the enumeration and exploitation path for the TryHackMe "Cyborg" room. The target had two open services: SSH and HTTP. A hidden Squid password file was discovered through web content enumeration, which led to the archive key and further access to a Borg backup archive.

## Target Information

- IP: `10.48.139.226`
- Open ports:
  - `22/tcp` - SSH
  - `80/tcp` - HTTP

## Enumeration

### Nmap

Initial port scan confirmed the service surface:

- `22/tcp` open ssh
- `80/tcp` open http

### Web enumeration

A directory scan against the HTTP service revealed the following interesting paths:

- `/admin` -> redirects to `/admin/`
- `/etc` -> redirects to `/etc/`
- `/index.html` -> application entry point
- `/server-status` -> server status page (403)

### Hidden data discovery

A hidden file was discovered under `/etc/squid/passwd`:

- `music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.`

This indicated a stored Apache MD5 password hash for the `music_archive` account.

## Password recovery

The hash was cracked with Hashcat using `-m 1600` (Apache MD5) and a wordlist.

Command used:

```bash
hashcat -a 0 -m 1600 hash /usr/share/SecLists/rockyou.txt --force
```

Result:

- `music_archive` password: `squidward`

## Backup archive analysis

The discovered credentials and artifacts pointed to a Borg backup archive. The archive path used in this investigation was:

- `archive/home/field/dev/final_archive/::music_archive`

The Borg archive listing revealed a user home directory and several files belonging to `alex`.

## Findings

- The machine exposes standard services for a web-based challenge.
- Sensitive data is exposed through a hidden Squid password file.
- The `music_archive` hash was successfully cracked to `squidward`.
- The Borg backup archive contains a user profile for `alex` and additional data for further exploitation.

## Next steps

1. Use the recovered password to access the Borg archive.
2. Extract relevant files from `home/alex`.
3. Search for credentials or configuration data that enable privilege escalation.
4. Identify and exploit any local misconfigurations or backup-related attack paths.

## Notes

- The URL `https://borgbackup.readthedocs.io/` is the Borg documentation reference and confirms the backup tooling used in the box.
- The main pivot point in this challenge is the backup archive rather than a direct web application exploit.
- From the backup contents, focus on user `alex` and any stored secrets or configuration files.
