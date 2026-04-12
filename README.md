# snow-crash

This project contains solutions and explanations for the **Snow Crash** CTF, a series of cybersecurity challenges focused on Linux exploitation, reverse engineering, and script analysis.

## Level Overview

| Level | Topic | Description |
| :--- | :--- | :--- |
| **Level 00** | Caesar Cipher | Finding hidden files and decoding a ROT11/Caesar cipher. |
| **Level 01** | Password Cracking | Extracting a hashed password from `/etc/passwd` and cracking it using John The Ripper. |
| **Level 02** | Network Traffic | Analyzing a `.pcap` file with Wireshark to find cleartext credentials in a TCP stream. |
| **Level 03** | PATH Injection | Explaining a SUID binary that calls `echo` without an absolute path to hijack the execution. |
| **Level 04** | Perl Script Injection | Exploiting a Perl CGI script that uses backticks with unvalidated parameters. |
| **Level 05** | Cron Jobs | Exploiting a scheduled task (cron) that executes files from a world-writable directory. |
| **Level 06** | PHP `/e` Exploit | Using the deprecated `/e` modifier in `preg_replace` to execute arbitrary code. |
| **Level 07** | Environment Variables | Manipulating the `LOGNAME` environment variable to inject commands into a `system()` call. |
| **Level 08** | Symlink Bypass | Bypassing a filename check (`token`) by using a symbolic link. |
| **Level 09** | Progressive Cipher | Reversing a custom rotation cipher using a dedicated Python script. |
| **Level 10** | Race Condition | Using a symbolic link race condition to bypass an `access()` check before an `open()` call. |
| **Level 11** | Lua Command Injection | Injecting shell commands through an unescaped `io.popen` call in a Lua server. |
| **Level 12** | Perl Wildcard & Backticks | Combining backticks injection with shell wildcards to bypass uppercase filtering. |
| **Level 13** | Register Manipulation | Using GDB to force the return value of `getuid()` in a SUID binary. |
| **Level 14** | Anti-Debugging & GDB | Bypassing `ptrace` checks and emulating a specific UID in GDB to extract the final token. |

## Structure

Each level has its own directory containing:
- `flag`: The solution token for the level.
- `resources/Readme.md`: A detailed walkthrough of the tools used, the vulnerability found, and the step-by-step solution.

## Quick Start

To explore a specific level, navigate to its directory:

```bash
cd levelXX/resources
cat Readme.md
```

