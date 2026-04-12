# Level14

### Tools

### How to solve it

1. After logging in using ssh at level14@(vmIP):

```bash
ssh level14@000.000.000.000 -p 4242
```

2. The program checks the UID and the flag user is visible in `/etc/passwd`:

```bash
flag14:x:3014:3014::/home/flag/flag14:/bin/bash
```

   That means the correct ID to emulate is `3014`.

3. The `disas main` output shows the exact code that does it:

```gdb
0x08048982 <+60>:    movl   $0x0,(%esp)
0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
0x0804898e <+72>:    test   %eax,%eax
0x08048990 <+74>:    jns    0x80489a8 <main+98>
```

   That means the program calls `ptrace()` first. It checks the return value in `%eax` and only continues if that return is non-negative. In a debugger, `ptrace` can fail, so the program would stop.

   Later it requires `3014` in `%eax`, which is why the second breakpoint sets `%eax=3014`.

4. In GDB, set `%eax` to the needed values at the breakpoints and continue:

```gdb
(gdb) break *0x0804898e
Breakpoint 1 at 0x804898e
(gdb) break *0x08048b0a
Breakpoint 2 at 0x8048b0a
(gdb) run
Starting program: /bin/getflag

Breakpoint 1, 0x0804898e in main ()
(gdb) set $eax=0
(gdb) c
Continuing.

Breakpoint 2, 0x08048b0a in main ()
(gdb) set $eax=3014
(gdb) c
Continuing.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
[Inferior 1 (process 2941) exited normally]
```

### How to protect

- Do not rely on `ptrace` anti-debug without additional checks.
- Do not use UID as the only gate for token release.


