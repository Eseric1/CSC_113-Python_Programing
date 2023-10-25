# Eric Samano 10/20/23
# Lab 4

## 6-3. Glossary
programming_terms = {
    'List':'Used to store multiple items in a single variable.',
    'Variables': 'Described as boxes to store values in or labels to store value in. ',
    'Whitespace':'Refers to any nonprinting character.',
    'Looping':'Automating repetetive task.',
    'Tuple':'An immutable list.',
    'Nesting':'Putting code inside other code.',
    'Program':'Set of instructions to perform specific action.',
    'Function':'Reusable block of code.',
    'Debugging':'Process of detecting and removing issues with the code.',
    'IDE':'Acronym standing for Integrated Development Environment.'
}
print(f'List: {programming_terms.get("List")}\n')
print(f'Variables: {programming_terms.get("Variables")}\n')
print(f'Whitespace: {programming_terms.get("Whitespace")}\n')
print(f'Looping: {programming_terms.get("Looping")}\n')
print(f'Tuple: {programming_terms.get("Tuple")}\n')

## 6-4. Glossary 2
for key, value in programming_terms.items():
    print(f'{key}: {value}\n')


## 6-5. Rivers
river= {
    'Tigris':'Turkey',
    'Euphrates':'Iraq',
    'Mississippi':'United States'
}
# Printing river with which countries they run through
for key, value in river.items():
    print(f'The {key} river runs through {value}')
# Printing the names of the river
for key in river:
    print(key)
# Printing the countries the rivers run through
for value in river.values():
    print(value)


## 6-8. Pets
Pets=[]

pet1 = {'animal': 'dog', 'owner': 'Alice', 'characteristic': 'loud' }
pet2 = {'animal': 'cat', 'owner': 'Bob', 'characteristic': 'agile'}
pet3 = {'animal': 'rabbit', 'owner': 'Charlie', 'characteristic': 'fast'}
pet4 = {'animal': 'ferrit', 'owner': 'Shayne', 'characteristic': 'hairy'}
pet5 = {'animal': 'gerbil', 'owner': 'Chance', 'characteristic': 'fat'}
pet6 = {'animal': 'parrot', 'owner': 'Amy', 'characteristic': 'colorful'}

# Adding pets to the list
Pets.append(pet1)
Pets.append(pet2)
Pets.append(pet3)
Pets.append(pet4)
Pets.append(pet5)
Pets.append(pet6)

# printing full statement
for pet in Pets:
    print(f"The {pet['animal']} belongs to {pet['owner']} and is {pet['characteristic']}.")


## 6-11. Cities
#Dictionary
cities = {
    'phoenix': {
        'country': 'USA',
        'population': '1.61 million',
        'fact': 'tempatures constantly exceed 100 degrees farenheit'
        },

    'seattle': {
        'country': 'USA',
        'population':'753,675',
        'fact':'it is the birthplace of Starbucks and the grunge music genre'

    },

    'los angeles': {
        'country': 'USA',
        'population': '3.99 million',
        'fact':  'it is the home of Hollywood and the entertainment industry'
    }
}
# Printing Statement
for city, info in cities.items():
    print(f"{city.title()} resides in {info['country']} and has a population of {info['population']} and {info['fact']}.")