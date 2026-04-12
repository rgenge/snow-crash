# Level13

### Tools

### How to solve it

1. After logging in using ssh at level13@(vmIP):

```bash
ssh level13@000.000.000.000 -p 4242
```

2. The strings from the binary show `getuid` and the message `UID %d started us but we we expect %d`, so we know the program checks the user ID before giving the token.

   From your GDB run, the program printed:

   ```
   UID 2013 started us but we we expect 4242
   ```

   That tells us the expected UID is exactly `4242`, not `42`.

3. The disassembly confirms it: `main` calls `getuid()`, then compares `%eax` with `0x1092`.

   The full `disas main` output is:

   ```gdb
   (gdb) disas main
   Dump of assembler code for function main:
      0x0804858c <+0>:     push   %ebp
      0x0804858d <+1>:     mov    %esp,%ebp
      0x0804858f <+3>:     and    $0xfffffff0,%esp
      0x08048592 <+6>:     sub    $0x10,%esp
      0x08048595 <+9>:     call   0x8048380 <getuid@plt>
      0x0804859a <+14>:    cmp    $0x1092,%eax
      0x0804859f <+19>:    je     0x80485cb <main+63>
      0x080485a1 <+21>:    call   0x8048380 <getuid@plt>
   ```

   This means the program does:
   - call `getuid()` to get the current UID;
   - compare the return value in `%eax` with `0x1092`;
   - if equal, jump to the token path;
   - if not equal, continue to the failure path.

   `0x1092` in decimal is `4242`, so the check is exactly `getuid() == 4242`.

   The run that ended with `[Inferior 1 (process 2746) exited with code 01]` is the failure path because the real UID was not `4242`.

4. Use GDB to force the return value of `getuid()` to `4242` instead of your real UID.

```gdb
(gdb) b *0x0804859a
Breakpoint 1 at 0x804859a
(gdb) run
Starting program: /home/user/level13/level13

Breakpoint 1, 0x0804859a in main ()
(gdb) set $eax=4242
(gdb) c
Continuing.
your token is 2A31L79asukciNyi8uppkEuSx
[Inferior 1 (process 2786) exited with code 050]
```

### How to protect

- Do not trust UID-based checks alone.
- Avoid relying on client-side or user-controlled process state for token release.


