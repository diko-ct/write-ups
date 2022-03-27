# meet_me_in_middle


![sh](https://user-images.githubusercontent.com/75040566/160281114-312530e9-eb12-4456-a67f-28918c6fa52a.png)

i got the encrypted flag and source code and it's like the title clarify (meet me in middle attack )

```python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
padding = b"0fpptCTF5!@#"
ciphertext = bytes.fromhex('187f25ea856f518bcd8e7e7c17e7e6016bc77459513740e6792c84d07b465ea9cee6609881421eb4ae1606792a2d8859')
custom_plaintext = pad(bytes.fromhex('4f465050542d435446'),16)
custom_ciphertext = bytes.fromhex('f71f3b195e2336a6d30077b8184304c6')

alpha = b'0123456789abcdef'
ciphertext1 = {}
for a in alpha:
    for b in alpha:
        for c in alpha:
            for d in alpha :
                per =bytes([a,b,c,d])
                key = padding + per
                cipher1 = AES.new(key , AES.MODE_ECB)
                ciphertext1[cipher1.encrypt(custom_plaintext)] = key

plaintext1 ={}
for a in alpha:
    for b in alpha:
        for c in alpha:
            for d in alpha :
                per =bytes([a,b,c,d])
                key2 =  per + padding
                cipher2 = AES.new(key2 , AES.MODE_ECB)
                plaintext1[cipher2.decrypt(custom_ciphertext)] = key2
ciphertext1_set = set(ciphertext1.keys())
plaintext1_set = set(plaintext1.keys())
inter = ciphertext1_set.intersection(plaintext1_set)


for i in inter :

        key1 = ciphertext1[i]
        key2 = plaintext1[i]
        break
cipher1 = AES.new(key1,AES.MODE_ECB)
cipher2 = AES.new(key2,AES.MODE_ECB)
print(cipher1.decrypt(cipher2.decrypt(ciphertext)))


```

flag is : OFPPT-CTF{M33t_1n_Th3_Middle_4tt4ck_4_RS4}
