# .#
![hash](https://user-images.githubusercontent.com/75040566/189964472-e05582f1-cce3-4508-8ce2-1438198209b4.png)



```python
import hashlib
from random import shuffle  , randint
f=open('wordlist.txt','rb').readlines()


shuffle(f)

word = f[randint(0 , len(f))].decode().strip('\n')

def enc(w):
	r = ''
	for i in w[::-1]:
		r+= hashlib.sha256(hashlib.md5(i.encode()).hexdigest().encode()).hexdigest()
	return r

print('c = ' , enc('???')+enc(word)[3:]) 
```
```
c =  db2d8e82412b775f358732deba189805318d3bb40008c333171f078dcd4be0b8787ef811dc588e955c76e8ad3cf14485460d4030bedb99a13b23779236c3473b1344753c604c4f994a6a428dfca4698408cbbd50ac019f34d13eb2aa64ecf7138d95924c019274d7de2c329ffab4e1ed009cac6e0c4dd29bab4839adc2aec94efefa2dc48d2a631176515e7fac1a0071e6b6a7fc3aa13b0d793b08dca59cd6b752480911b6e43e6a78a4fe020f13abc5df6ddcb9bf0c33ab401c3c327a1f4da07a2e00bec7450aa75174e0d10bc8b80430cf6a3f91308ce10aa8526b27a793f515b0e944598d03f5cb197d56dbd835720e02cd2305c5e27f09cf805efead79b0b7edebf85f1aef852317066b0acbc35db0fd3c36c00daf67f961c0d1e8574c356e0006c694856e8ead5cd673cbbe74590e011d869675ccec0a8ba72b1c16c418dd73df63bfe1dc9b1d126d340ccf4941198ccf573eff190a6ff8dc69e87e4a24b7ab10532f563fa436f59c068736fa29f3eee46012f5e9992b98f1cbee96f
```

as you can see i can't reverse hashes then i will use it , 
sha256 length as hex is 64 then i know that the first 192 char for '???'
and the rest for word 
for enc(word)[3:] == c[192:] i will brute force the word from rockyou.txt list 
and for enc('???') == c[:192] i will try to find ??? 

```python 
import hashlib
from random import shuffle 
from string import printable
from itertools import combinations , permutations

f=open('wordlist.txt','rb').readlines()

c =  'db2d8e82412b775f358732deba189805318d3bb40008c333171f078dcd4be0b8787ef811dc588e955c76e8ad3cf14485460d4030bedb99a13b23779236c3473b1344753c604c4f994a6a428dfca4698408cbbd50ac019f34d13eb2aa64ecf7138d95924c019274d7de2c329ffab4e1ed009cac6e0c4dd29bab4839adc2aec94efefa2dc48d2a631176515e7fac1a0071e6b6a7fc3aa13b0d793b08dca59cd6b752480911b6e43e6a78a4fe020f13abc5df6ddcb9bf0c33ab401c3c327a1f4da07a2e00bec7450aa75174e0d10bc8b80430cf6a3f91308ce10aa8526b27a793f515b0e944598d03f5cb197d56dbd835720e02cd2305c5e27f09cf805efead79b0b7edebf85f1aef852317066b0acbc35db0fd3c36c00daf67f961c0d1e8574c356e0006c694856e8ead5cd673cbbe74590e011d869675ccec0a8ba72b1c16c418dd73df63bfe1dc9b1d126d340ccf4941198ccf573eff190a6ff8dc69e87e4a24b7ab10532f563fa436f59c068736fa29f3eee46012f5e9992b98f1cbee96f'


def enc(w):
	r = ''
	for i in w[::-1]:
		r+= hashlib.sha256(hashlib.md5(chr(i).encode()).hexdigest().encode()).hexdigest()
	return r
	
	

for i in range(len(f)):
	w = f[i][:-1]
	if enc(w)[3:] == c[192:] :
		print(w.decode()) 
		break


p = permutations(printable, 3)

for i1 , i2 , i3   in p:
	
	if enc((i1+i2+i3).encode()) == c[:192]:
		print(i1,i2,i3)
		break

```

flag = yuctf{%G0janetrzig}
