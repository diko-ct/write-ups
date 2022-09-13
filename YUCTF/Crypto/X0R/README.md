#X0R 
```python
flag = b'yuctf{}'
key = b'********'
cipher = b''

for i in range(len(flag)):
	cipher+= chr(flag[i] ^ key[i%len(key)]).encode()
with open('cipher.enc' , 'wb') as f :
	f.write(cipher)
```

key length is 8  and you have the beginning of the flag : 'yuctf{'
the key = plain ^ cipher =    key = b'yuctf{'^ cipher[:6] 
key = b'perfec' and you can guess the 7th byte key = b'perfect'

the last byte you can brute force it 

```python

f = open('cipher.enc','rb').read()
from pwn import xor 
key = xor(b'yuctf{' , f[:6])
print(key)
key = b'perfect'
h = key 


for i in range(256):
	try:
	
		key = key+chr(i).encode()
		flag = xor(key , f)
		print(flag.decode())
		key = h 
	except:
		pass
```
or you can guess the last byte key = b'perfecto'
flag = yuctf{X0r_15_r3v3rsible}
