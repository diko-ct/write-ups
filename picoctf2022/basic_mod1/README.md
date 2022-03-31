# basic_mod1

![Screenshot_20220331_142337](https://user-images.githubusercontent.com/75040566/161044472-74014964-73cf-4430-b04d-3cb374948f83.png)


simple arithmetic :)

message.txt : 
```54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 ```


```python
h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
f = open('message.txt','r').read().split()
for i in f :
    print(h[(int(i) % 37)],end='')
```
