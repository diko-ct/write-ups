

# xorrox 
![Screenshot_20220429_102256](https://user-images.githubusercontent.com/75040566/166269166-7c84a55e-20f0-440e-a1ec-8f784670a9fe.png)


in this chall i have encryption code 
```python
import random

with open("flag.txt", "rb") as filp:
    flag = filp.read().strip()

key = [random.randint(1, 256) for _ in range(len(flag))]

xorrox = []
enc = []
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    xorrox.append(k)
    enc.append(flag[i] ^ v)

with open("output.txt", "w") as filp:
    filp.write(f"{xorrox=}\n")
    filp.write(f"{enc=}\n")

```
and output 
```
xorrox=[1, 209, 108, 239, 4, 55, 34, 174, 79, 117, 8, 222, 123, 99, 184, 202, 95, 255, 175, 138, 150, 28, 183, 6, 168, 43, 205, 105, 92, 250, 28, 80, 31, 201, 46, 20, 50, 56]
enc=[26, 188, 220, 228, 144, 1, 36, 185, 214, 11, 25, 178, 145, 47, 237, 70, 244, 149, 98, 20, 46, 187, 207, 136, 154, 231, 131, 193, 84, 148, 212, 126, 126, 226, 211, 10, 20, 119]

```

when i read the code i saw that he gave key bytes but it had been xored with each other right:).
so the first i don't know it because range(0 , 0 , -1 ) so he will give  1 . 
the seconde i can get by xoring 1 and 209 etc . 
then i can get all of the key except the first bytes but i can do bruteforce or i know the flag begin with f so f xor enc[0] = first byte
```python 
from pwn import xor
xorrox=[1, 209, 108, 239, 4, 55, 34, 174, 79, 117, 8, 222, 123, 99, 184, 202, 95, 255, 175, 138, 150, 28, 183, 6, 168, 43, 205, 105, 92, 250, 28, 80, 31, 201, 46, 20, 50, 56]
enc=[26, 188, 220, 228, 144, 1, 36, 185, 214, 11, 25, 178, 145, 47, 237, 70, 244, 149, 98, 20, 46, 187, 207, 136, 154, 231, 131, 193, 84, 148, 212, 126, 126, 226, 211, 10, 20, 119]
key = [ ]
k = []

print(len(xorrox))
for i,v  in enumerate(xorrox):
    k = v

    for j in range(i-1 , -1 , -1 ):
        k^=key[j]
    key.append(k)


print(len(key))
key[0] = 124
for i in range(38):
    print(xor(key[i] , enc[i]).decode(),end='')
print()

```
flag = flag{21571dd4764a52121d94deea22214402}
