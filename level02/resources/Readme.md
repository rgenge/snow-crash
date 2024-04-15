# Level00

### Tools
tcpdump


### How to solve it

1. After loging in using ssh in level02@(vmIP): 
```
ssh level02@000.000.000.000 -p 4242
```
2. We use the ls command and it shows a pcap file called level02.
```
level02.pcap
```
3. Then we have to try to check whats inside it we use tcpdump and get some ips communications.
```
tcpdump -r level02.pcap 
```
4. Now we have the password for su flag00, we login and run gettheflag
```
 x24ti5gi3x0ol2eh4esiuxias
```
### How to protect
 - Use better and improved enconding options
 - Try to hide better your passwords and never get it exposed in your machine
