#### Part A - Creating a Class
# I chose to represent a menu item as a class
class MenuItem:
    # The class has three attributes: name, price, and category
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    # A method to display the name and price of the item
    def show(self):
        return f"{self.name} the {self.category} for ${self.price} "
    
    # A method to apply a discount to the price of the item
    def apply_discount(self, percentage):
        self.price = round(self.price * (1 - percentage / 100), 2)
        print(f"Discount applied to {self.name}: ${self.price} ")

# Creating two instances of MenuItem
taco = MenuItem("Taco", 8.99, "Main")
salad = MenuItem("Salad", 5.99, "Side")

# Testing the methods
#taco.show()
#salad.show()
salad.apply_discount(10)


#### Part B - Inheritance
# Subclass of MenuItem called Drink
class Drink(MenuItem):
    # The subclass with two new attributes: size and ice
    def __init__(self, name, price, category, size, ice):
        super().__init__(name, price, category)
        self.size = size
        self.ice = ice
    
    # A method to display the size and ice preference of the drink
    def show_size_and_ice(self):
        print(f"{self.size} {self.name} with {'ice' if self.ice else 'no ice'}")
    
    # Overriding the show method to include the size and ice preference
    def show(self):
        return f"{self.size} {self.name} with {'ice' if self.ice else 'no ice'} for ${self.price}"

# Creating two instances of Drink
cola = Drink("Cola", 1.99, "Drink", "Small", True)
tea = Drink("Tea", 2.99, "Drink", "Large", False)


# Part C - Objects and Lists
# List of all menu items
menu = [taco, salad, cola, tea]

# Iterating through the list and displaying information
for item in menu:
    print(f'\nWelcome to our resturant we have a {item.show()}')
