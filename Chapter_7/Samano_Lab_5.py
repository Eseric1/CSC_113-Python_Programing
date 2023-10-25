# Eric Samano 
# 10/24/23
# Lab 5

#### 7-5 Movie Tickets
while True:
    person = int(input('Hi, Welcome to the movie theaters, how old are you? '))
    if person <= 3:
        price = 'free'
        print(f'Your ticket will be {price}. ')
        break

    elif person >= 3 and person <= 12:
        price = '$10'
        print(f'Your ticket will be {price}. ')
        break

    elif person > 12:
        price = '$15'
        print(f'Your ticket will be {price}. ')
        break

    else:
        break
    

#### 7-6 Three Exits
count = 0
age = input('Hi, Welcome to the movie theaters, how old are you? ')
while age != 'quit' and count < 5:
    # Convert user's input to integer
    person = int(age)

    # Use a break statement to exit the loop 
    if age == 'quit':
        break

    
    if person <= 3:
        price = 'free'
        print(f'Your ticket will be {price}. ')

    elif person >= 3 and person <= 12:
        price = '$10'
        print(f'Your ticket will be {price}. ')

    elif person > 12:
        price = '$15'
        print(f'Your ticket will be {price}. ')

    # Updating count variable
    count += 1

    # Ask the user's input again
    age = input('Hi, Welcome to the movie theaters, how old are you? ')


#### 7-8. Deli
sandwich_orders =['caprese','club','rueben',
                   'tuna','ham & cheese','veggie']
finished_sandwiches =[]

# Looping through sandwhich orders
for order in sandwich_orders:
    print(f'I made a {order} sandwhich')

    #as each sandwhich is made, move to list of finished sandwhiches
    finished_sandwiches.append(order)

# print messsage after sandwiches have been made
print('I have made the following sandwiches :')
for sandwich in finished_sandwiches:
    print(f'- {sandwich} sandwich')


