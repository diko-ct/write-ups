# impossible xor 

```python 
import os

flag = b"yuctf{}"#the flag just contains letters , digits , _ , {}

key=list(b'*******')
enc = b''
for i in range(len(flag)):

	
	enc+=  chr(flag[i] ^ key[i%len(key)]).encode()
	if i%len(key)==0:
		r = key[0]
		del key[0]
		key.append(r)

with open('secret.enc' , 'wb') as a:
	a.write(enc)
```
every time the key xored with the plain text it takes the first byte and insert it at the end 
```python 
enc= open('secret1.enc' , 'rb').read()

print('___________------------____________----')
key = list(xor(b'yuctf{' , enc[:6]))	 
plain= b''
plains=[]
for i in range(256):
	key = list(xor(b'yuctf{' , enc[:6]))	
	key = [key[0]  , i ] + key[1:]
	
	
	for j in range(len(enc)):
		plain+= chr(enc[j] ^ key[j%len(key)]).encode()
		if j%len(key)==0:
			r=key[0]
			del key[0]
			key.append(r)
			

	if plain[-1] == ord('}') :
		try : 
			plains.append(plain.decode())
		except:
			pass

	plain = b''
print(plains)
```


flag = yuctf{4_c0mpl3x_X0r_1mpl3m3ntat10n_w1ll_n0t_s0lve_Th3_pr0blem}
