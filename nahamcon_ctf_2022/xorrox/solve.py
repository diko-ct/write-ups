from pwn import xor
xorrox=[1, 209, 108, 239, 4, 55, 34, 174, 79, 117, 8, 222, 123, 99, 184, 202, 95, 255, 175, 138, 150, 28, 183, 6, 168, 43, 205, 105, 92, 250, 28, 80, 31, 201, 46, 20, 50, 56]
enc=[26, 188, 220, 228, 144, 1, 36, 185, 214, 11, 25, 178, 145, 47, 237, 70, 244, 149, 98, 20, 46, 187, 207, 136, 154, 231, 131, 193, 84, 148, 212, 126, 126, 226, 211, 10, 20, 119]
key = [ ]
k = []

print(len(xorrox))
for i,v  in enumerate(xorrox):
    k = v

    for j in range(i-1 , -1 , -1 ):
        k^=key[j]
    key.append(k)


print(len(key))
key[0] = 124
for i in range(38):
    print(xor(key[i] , enc[i]).decode(),end='')
print()
