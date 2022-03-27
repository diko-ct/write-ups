# XOR


![Screenshot_20220324_163903](https://user-images.githubusercontent.com/75040566/160281541-5e390732-f5d5-428b-a0a1-ee1f63bfb074.png)


```python
import os

FLAG = b'OFPPT-CTF{...REDACTED...}'


class HoneyComb:
    def __init__(self, key):
        self.vals = [i for i in key]

    def turn(self):
        self.vals = [self.vals[-1]] + self.vals[:-1]

    def encrypt(self, msg):
        keystream = []
        while len(keystream) < len(msg):
            keystream += self.vals
            self.turn()
        return bytes([msg[i] ^ keystream[i] for i in range(len(msg))]).hex()

hc = HoneyComb(os.urandom(6))

print(hc.encrypt(FLAG))

```

first it creates a key of length 6 bytes then if lenght of key < lenght message it adds the of the key to another variable then it shifts the key 

becuase the key is too small we know that the flag begin with OFPPT- we can xor first six bytes of ciphertext with first six bytes and we get the key then we can xor it with the ciphertext and every 6 bytes we can shift the key 


```python 
from pwn import xor

plaintext =b'OFPPT-'
ciphertext = bytes.fromhex('48ac3fe745bed053ac14ef2163cc70db58dfe862fe33860330dc22ea589c9f03d922e13365db038626eaee')

key = xor(plaintext, ciphertext[:6])
keyst =[]
for i in key :
    keyst.append(i)




keystream = []
while len(keystream) < len(ciphertext):
    keystream += keyst
    keyst =[keyst[-1]] + keyst[:-1]



print(xor(keystream , ciphertext))



```

flag is : OFPPT-CTF{X0r_w17h_sm4ll_k3y_vuln3r4b1l17y}
