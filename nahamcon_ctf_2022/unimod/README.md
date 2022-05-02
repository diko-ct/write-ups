
# unimod

![Screenshot_20220429_103932](https://user-images.githubusercontent.com/75040566/166264683-f29592fa-8967-4650-a15e-c68564d6d874.png)

in this chall he gave me encryption code 
```python 
import random

flag = open('flag.txt', 'r').read()
ct = ''
k = random.randrange(0,0xFFFD)
for c in flag:
    ct += chr((ord(c) + k) % 0xFFFD)

open('out', 'w').write(ct)

```
he picks a random key between 0 and 65533
so key < 10e9 then we can do a bruteforce . 


```python

f = open('out','r').read()
print(f)

for i in range(0 , 0xFFFD ):
    h = ''
    for j in f:
        h+= chr(( ord(j) -i )% 0xFFFD)
    if 'flag' in h :
        print(h)
```

flag: flag{4e68d16a61bc2ea72d5f971344e84f11}
