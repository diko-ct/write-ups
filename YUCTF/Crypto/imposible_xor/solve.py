import os
from pwn import xor  
from string import printable

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


for i in plains:
	print(i)
print(len(plains))
