# baby_rsa


![baby_rsa](https://user-images.githubusercontent.com/75040566/189963111-9b4aae32-a11e-45f4-af86-5489139a513a.png)




```python 
from Crypto.Util.number import getPrime , bytes_to_long
flag = bytes_to_long(b'flag')
p = getPrime(128)
q= getPrime(128)
n = p*q
e= 0x10001

print('N' , n )
print('e' , e )
print('c' , pow(flag,e,n))
```
```
N = 37874574128647474327888043811285407624047774749104265908566998093360576139729
e = 65537
c= 12840964582137722562097619108422133203142059133776777903614969689636661556132
```

as we can see p and q is very small then N is small as will 

we can use sagemath or factordb to get q ,  p  

```python
from Crypto.Util.number import getPrime , bytes_to_long , long_to_bytes

p = 218699414623435001817252801877626048461
q=173180957954832030279714219712458464789
n = 37874574128647474327888043811285407624047774749104265908566998093360576139729
e = 65537
c= 12840964582137722562097619108422133203142059133776777903614969689636661556132

phi = (p-1)*(q-1)
d = pow(e,-1,phi)
print(long_to_bytes(pow(c,d,n)))
```


flag = yuctf{Sm4ll_Mod_4r3_Y0u_1n5an3}
