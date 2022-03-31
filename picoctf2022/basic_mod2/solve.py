
import string
h = '.'+string.ascii_lowercase+'0123456789'+'_'
f = open('message.txt').read().split()
for i in f:
    print(h[pow((int(i)%41) , -1 , 41)],end='')
