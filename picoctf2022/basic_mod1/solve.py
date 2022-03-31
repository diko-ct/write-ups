h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
f = open('message.txt','r').read().split()
for i in f :
    print(h[(int(i) % 37)],end='')
