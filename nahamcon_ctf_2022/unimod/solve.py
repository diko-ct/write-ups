
f = open('out','r').read()
print(f)

for i in range(0 , 0xFFFD ):
    h = ''
    for j in f:
        h+= chr(( ord(j) -i )% 0xFFFD)
    if 'flag' in h :
        print(h)
