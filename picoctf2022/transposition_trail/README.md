#  transposition_trail


![Screenshot_20220331_162738](https://user-images.githubusercontent.com/75040566/161066108-3c5187df-4c4b-4c4d-bdbc-974f84b383fd.png)


if we take the first block we can see that the first char became the last : heT = The


```python

f = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4'


for i in range(0 , len(f) ,3 ):
    print(f[i+2] + f[i] + f[i+1] ,end='')


```


the flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
