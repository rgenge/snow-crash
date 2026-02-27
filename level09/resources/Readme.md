# Level09

### Tools


### How to solve it

1. After logging in using ssh at level09@(vmIP):
```
ssh level0@000.000.000.000 -p 4242
```
2. When logging in, we get these files:
```
level09 and token
```
3. We verify level09 is an executable, and by running it with 12345, we discover it uses a progressive cipher with rotation logic:
```
1   2   3   4   5
1   3   5   7   9
+0  +1  +2  +3  +4

```
4. With a simple python script, we are able to reverse this with a loop that subtracts it's value:
```
def decode_level09(data):
    decoded = bytearray()
    i = 0

    for b in data:
        value = b - i

        # keep value inside valid byte range (0–255)
        if value < 0:
            value += 256

        decoded.append(value)
        i = i + 1

    return decoded.decode(errors="ignore")

```
5. The token file contains encoded data like f4kmm6p|=�p�n��DB�Du{��. Applying our decode script gives us:
```
f3iji1ju5yuevaus41q1afiuq

```
6. Now that we have the password we run su flag09 and:
```
s5cAJpM8ev6XHw998pRWG728z
```

### How to protect
 - Do not use simple shift cipher for encryption
 - Implement proper encryption algorithms like AES, RSA, or other cryptographic standards
