# Level00

### Tools
John The Ripper 

### How to solve it

1. After getting the first flag we try the same command from flag00, it did not work, then we tried:
```
cat /etc/passwd
```
2. Then we have many files and one name gets our attention :
```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```
3. We use that with John The Ripper and get in return : 
```
 abcdefg
```
4. Now we have the password for su flag01, we login and run gettheflag
```
f2av5il02puano7naaf6adaaf
```
### How to protect
 - Use better and improved enconding options
 - Try to hide better your passwords and never get it exposed in your machine
