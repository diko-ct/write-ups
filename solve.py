from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

import os 


ciphertext = bytes.fromhex('8c5f0e4dbf1ba3293d71a147294f10e89b75e635122ffc1b')

KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)
