#Eric Samano

##5-4: Alien Colors #2
alien_color = 'green'
if alien_color == 'green':
    print ('earned 5 points ,GOOD JOB !')
else:
    print('earned 10 points')


##5-5: Alien Colors #3
alien_color = 'green'
if alien_color == 'green':
    print ('earned 5 points')
elif alien_color == 'yellow':
    print('earned 10 points')
elif alien_color == 'red':
    print('earned 15 points')


##5-6. Stages of Life
age = input('Hi, How old are you? ')

if int(age) <= 2:
    print('you are a baby!')
elif int(age) >=2 and int(age) < 4 :
    print('you are a toddler!')
elif int(age) >=4 and int(age) < 13 :
    print('you are a teenager')
elif int(age) >=20 and int(age) < 65 :
    print('you are an adult')
elif int(age) > 65:
    print('you are an elder')
    

##5-8. Hello Admin
logon = input('Hi, Please login using your username:')

if logon == 'admin':
    print(f'Hi welcome {logon}, you successfully logged in as admin, do you want to see the information ?')
else:
    print(f'Welcome {logon}, good to see you again.')


##5-9. No Users
users = ['eric']

if input('Whats your user name: ') == users:
    print('Hi.') 
else:
    print('We need to add more users!')

##5-10. Checking Usernames

current_users = ['eric1532','john235','terri0239','ericssaa1','ycycyc1']
new_users = ['eric1532','john235','terri023944','ericssaa144','ycycyc144']

for new_users in current_users:
    if new_users == current_users:
        print(f'{new_users}, you need to create a new username!')
    else:
        ('username is available')

##5-11. Ordinal Numbers

