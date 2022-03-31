# basic_mod2 
![Screenshot_20220331_142844](https://user-images.githubusercontent.com/75040566/161045220-38d15825-0b12-46f5-b7d7-192cab5bddaa.png)


message.txt:```268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186```

```python
import string
h = '.'+string.ascii_lowercase+'0123456789'+'_'
f = open('message.txt').read().split()
for i in f:
    print(h[pow((int(i)%41) , -1 , 41)],end='')

```
