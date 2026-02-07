# Level00

### Tools
https://gchq.github.io/CyberChef

Videos from intranet of 42

### How to solve it
1. If you watch the videos it talks about finding files used by flag00 user : 
```
find / -user flag00 2> /dev/null searches for files in the root directory (/) that are owned by the user flag00,
```
2. Then we have two files and using cat we get .
```
 cdiiddwpgswtgt
```
3. We try to su flag00 but the password doesnt'work, so it is encoded, then we try cyberchef, and using ROT13 with 11 that is Caesar Cipher we get :
```
 nottoohardhere
```
4. Now we have the password for su flag00, we login and run gettheflag
```
 x24ti5gi3x0ol2eh4esiuxias
```
### How to protect
 - Use better and improved enconding options
 - Try to hide better your passwords and never get it exposed in your machine
