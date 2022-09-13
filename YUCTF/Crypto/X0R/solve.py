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
	
