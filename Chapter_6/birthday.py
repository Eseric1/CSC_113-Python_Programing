birthday = {}

print ('Hi welcome to the birthday dictionary\n')

while True:
    # lookup statement
    response = str(input('Would you like to lookup someones birthday ? \n')).lower()
    if response == 'yes':
        
        lookup = str(input('Ok whos birthday are you looking for? : \n')).title()
        if lookup in birthday:
                print(f"{lookup}'s birthday is {birthday[lookup]} ")
        else: 
            print ()
            birthday_append = (input(f'Sorry {lookup} is not in our database, please add them, following this format; Name, mm/dd/yyyy: ')).title()
            key, value = birthday_append.split(',') 
            # stripping whitespace from inputs
            key = key.strip()
            value = value.strip()
            # appendding key-value pair to the dictionary
            birthday[key]= value
            print(f'Great, {key} was added to the list with his birthday {value}\n')
                

    elif response == 'no': 
        add_birthday=input('Ok you dont want to look up a birthday, would you like to add a an entry ?\n').lower()  

        if add_birthday == 'yes':
            
            birthday_append = (input('Ok great Enter the name and the birthday separated by a comma like so; Amy, 10/2/1999:\n')).title()
            key, value = birthday_append.split(',') 
            # stripping whitespace from inputs
            key = key.strip()
            value = value.strip()
            # appendding key-value pair to the dictionary
            birthday[key]= value
            print(f'Great, {key} was added to the list with his birthday {value}\n')
            continue

        else :
            change_birthday = input('You dont want to lookup or add a birthday, do you want to change a birthday?\n').lower()
            if change_birthday == 'yes':
                name = input('Enter the name of the person whose birthday you want to change: \n').title()
                new_birthday = input(f'Enter the new birthday for {name} in mm/dd/yyyy format: \n')
                birthday[name] = new_birthday
                print(f'Great, {name}\'s birthday was changed to {new_birthday}\n')
                continue
            else:
                delete_user = input('Would you like to delete a person ? :\n').lower()
                if delete_user == 'yes':
                    delete = input('Who would you like to delete? :\n').lower
                    # Delete info
                    birthday.pop(delete, None)
                    # print a confirmation message
                    print(f'Great, {delete} and their birthday were deleted from the list.\n')
                else :
                    quit=input('Would you like to quit the program?\n').lower()
                    if quit == 'yes':
                        print('Ok, Goodbye')
                        break
                    
        