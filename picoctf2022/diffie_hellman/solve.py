

p = 13
g = 5
a = 7
A = pow(g,a,p)
b = 3
B = pow(g,b,p)
print(pow(B , a , p ))
print(pow(A , b , p ))
print(B+a)
print(A+b)
from Crypto.Util.number import bytes_to_long , long_to_bytes
from string import ascii_uppercase
h = 'H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_D9FF6IFD'
q = ascii_uppercase+'0123456789'
for i in h :
    if i != '_':
        print(q[(q.index(i) - 5 )%36],end='')
    else:
        print(i,end='')
