## 3-2: Greetings

#List of Names
names =['Kevin','Larry','Terri','Tracy','John']
#Greetings
print(f'Hi,{names[0]}, I hope your doing well , lets catch up!')
print(f'Hi,{names[1]}, I hope your doing well , lets catch up!')
print(f'Hi,{names[2]}, I hope your doing well , lets catch up!')
print(f'Hi,{names[3]}, I hope your doing well , lets catch up!')
print(f'Hi,{names[4]}, I hope your doing well , lets catch up!')


## 3-4: Guest List
# Guest List
Guest_names =['Kent','Leonard','Terrence','Trent','Johnston']
# Dinner Invites
print(f'Hi,{Guest_names[0]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[1]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[2]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[3]}, I would like to invite you to dinner tonight, lets catch up!')


## 3-5. Changing Guest List
# Announcing who wont be able to make it
print(f'Hi everybody,{Guest_names[4]} wont be able to make it tonight to dinner')
# Adjusting guest list
del Guest_names[4]
Guest_names.insert(4,'Terrenson')
#new invite to Terrenson
print(f'Hi,{Guest_names[4]}, I would like to invite you to dinner tonight, lets catch up!')

##3-6. More Guests
print(f'Hi,{Guest_names[0]}, I found a bigger dinner table for tonight')
print(f'Hi,{Guest_names[1]}, I found a bigger dinner table for tonight')
print(f'Hi,{Guest_names[2]}, I found a bigger dinner table for tonight')
print(f'Hi,{Guest_names[3]}, I found a bigger dinner table for tonight')
print(f'Hi,{Guest_names[4]}, I found a bigger dinner table for tonight')

# inserting names to my guest list
Guest_names.insert(0,'Sean')
Guest_names.insert(3,'Seanston')
Guest_names.insert(7,'Shaun')

print(Guest_names)

print(f'Hi,{Guest_names[0]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[1]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[2]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[3]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[4]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[5]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[6]}, I would like to invite you to dinner tonight, lets catch up!')
print(f'Hi,{Guest_names[7]}, I would like to invite you to dinner tonight, lets catch up!')

##3-7. Shrinking Guest List
print(f'Hi,{Guest_names[0]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[1]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[2]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[3]}, I have terrible news our table was changed and I can only invite two people, I would love if you could still make it')
print(f'Hi,{Guest_names[4]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[5]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[6]}, I have terrible news our table was changed and I can only invite two people, maybe next time we can catch up')
print(f'Hi,{Guest_names[7]}, I have terrible news our table was changed and I can only invite two people, I would love if you could still make it')

print (Guest_names)

Guest_names.pop(0)
Guest_names.pop(0)
Guest_names.pop(0)
Guest_names.pop(1)
Guest_names.pop(1)
Guest_names.pop(1)

del Guest_names[0]
del Guest_names[0]


print (Guest_names)

##  4-2. Animals
# animal list
animals = ['Otter','Shark','Duck']
# for loop
for animal in animals:
    print(f'The {animal} loves water.')
print('all these animals love water.')

## 4-3. Counting to Twenty
#Setting range
for value in range(1,21):
    print(value)

## 4-7. Threes
for value in range(0,11):
    three= value * 3
    print(three)

## 4-10. Slices
print (f'The First three names on the list are{names[0:3]}')
print (f'Three names on the list are{names[1:4]}')
print (f'The Last three names on the list are{names[-3:]}')








