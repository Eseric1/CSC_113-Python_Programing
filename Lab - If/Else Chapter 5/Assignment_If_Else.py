#Eric Samano


break_message = ('You decided to quit the program.')
numbers = []

## Number 1 Input Loop
while True:
    

    number_1 = int(input('Hi. please give me your First number (0 to stop) :'))
    if number_1 == 0:
        print(break_message)
        break
# Adding number to list & breaking this loop  
    numbers.append(number_1)
    print('Great your number was added.\n')
    break
        
## Number 2 Input Loop
while True:
    number_2 = int(input('Please give me your Second number (0 to stop) :'))
    if number_2 == 0:
        print(break_message)
        break

# Making sure no duplicate numbers exist & resetting the Loop
    if number_2 in numbers:
        print('Sorry that number already exist, give me another')
        print(f'these are the number saved{numbers}\n')
        continue
# Adding number to list & breaking this loop  
    else:
        numbers.append(number_2)
        print('Great your numbers was added.\n')
        break


## Number 3 Input Loop       
while True:     
    number_3 = int(input('Please give me your Third number (0 to stop) :'))
    if number_3 == 0:
        print(break_message)
        break

# Making sure no duplicate numbers exist & resetting the Loop
    if number_3 in numbers:
        print('Sorry that number already exist, give me another')
        print(f'these are the numbers saved{numbers}\n')
        continue
# Adding number to list & breaking this loop  
    else:
        numbers.append(number_3)
        print('Great your number was added.\n')
        break

## Number 4 Input Loop       
while True:
    number_4 = int(input('Please give me your Last number (0 to stop) :'))
    if number_4 == 0:
        print(break_message)
        break

# Making sure no duplicate numbers exist & resetting the Loop
    if number_4 in numbers:
        print('Sorry that number already exist, give me another')
        print(f'these are the numbers saved so far {numbers}.\n')
        continue
    # Adding number to list & breaking this loop  
    else:
        numbers.append(number_4)
        print('Great your number was added.')
        print(f'Here is your list of numbers{numbers}')
        print('The program has concluded.')
        break
