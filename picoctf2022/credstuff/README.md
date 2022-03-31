# credstuff 

![Screenshot_20220331_143509](https://user-images.githubusercontent.com/75040566/161046235-e023ff67-190c-4485-807f-78a58d8ae1fc.png)


frist , try to map between passwords.txt and usernames.txt to find password 

```python 
pas = open('passwords.txt','r').readlines()
user = open('usernames.txt','r').readlines()
for index, i in enumerate(user):
    if i.strip() ==  'cultiris':
        print(pas[index])
```
output : cvpbPGS{P7e1S_54I35_71Z3}
and it's look like rot 

flag : picoCTF{C7r1F_54V35_71M3}
