cipher = list('ut{4c_3i_0_4}cch_YcytfNMfu')
for i in range(len(cipher) , -1 , -1):
    for j in range(  len(cipher) - 2  , i-1 , -1):
        cipher[j] , cipher[j+1] = cipher[j+1],cipher[j]
print(''.join(cipher))
