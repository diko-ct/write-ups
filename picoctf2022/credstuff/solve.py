pas = open('passwords.txt','r').readlines()
user = open('usernames.txt','r').readlines()
for index, i in enumerate(user):
    if i.strip() ==  'cultiris':
        print(pas[index])
#then rot13
