# Eric Samano 11/1/23
# Lab 9

#### Exercise 9-6: Ice Cream Stand


class Restaurant:
    # Store two attributes, restaurant name and cuisine type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # A method that prints a message indicating that the restaurant is open
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant that is open for business.")

# Class that inherits from Restaurant class
class IceCreamStand(Restaurant):
    # Added an attribute called flavors
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    # Method that displays these flavors
    def show_flavors(self):
        print(f"The ice cream stand offers the following flavors: {', '.join(self.flavors)}.")

# Create an instance of IceCreamStand and call this method
ice_cream_stand = IceCreamStand("Ben & Jerry's", "Ice Cream", ["Chocolate Chip Cookie Dough", "Cherry", "Vanilla"])
ice_cream_stand.show_flavors()


#### Exercise 9-7: Admin

class User:
    # Two attributes called first_name and last_name & other attributes 
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    # Method called describe_user() that prints a summary of the user's information
    def describe_user(self):
        print(f"User profile summary:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    # Method called which prints a personalized greeting 
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our website.")

# Class called Admin that inherits from the User class
class Admin(User):

    # Added 'privileges' attribute 
    def __init__(self, first_name, last_name, username, email, location, privileges):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = privileges

    # Write a method called show_privileges that lists the admin's set of privileges
    def show_privileges(self):
        print(f"The admin has the following privileges: {', '.join(self.privileges)}.")

# Create an instance of Admin and call your method
admin = Admin("Alice", "Smith", "alice_smith", "alice.smith@example.com", "New York", ["can add post", "can delete post", "can ban user"])
admin.show_privileges()

## Exercise 9-8: Privileges

# Separate Priviliges class
class Privileges:
    # The class with one attribute
    def __init__(self, privileges):
        self.privileges = privileges

    # Move the show_privileges() method to this class
    def show_privileges(self):
        print(f"The admin has the following privileges: {', '.join(self.privileges)}.")

# Write a class called Admin that inherits from the User class
class Admin(User):
    # Make a Privileges instance as an attribute in the Admin class
    def __init__(self, first_name, last_name, username, email, location, privileges):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges(privileges)

# New instance of Admin and using method to show privileges
admin = Admin("Alice", "Smith", "alice_smith", "alice.smith@example.com", "New York", ["can add post", "can delete post", "can ban user"])
admin.privileges.show_privileges()


## Exercise 9-9: Battery Upgrade
class Car:
    """A simple attempt to represent a car """
    # Class with several attributes about the car
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Method to give the user details of the car
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    # Method to read odometer
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    # Method to read odometer
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back the odometer!')

    # Method to add miles in increments
    def increment_odometer(self, miles):
        self.odometer_readings += miles

# Battery Class
class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    # Method describing the battery size
    def desibe_battery(self):
        print(f'This car has a {self.battery_size} - kWh battery.')

    # Method describing the battery size and range
    def get_range(self):
        if self.battery_size ==75:
            range =260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')

    # Method upgrading the battery and printing size and range
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def fill_gas_tank(self):
        print(f'This car doesnt need a gas tank')



my_tesla = ElectricCar('tesla','model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print("\n-- Original Battery --")
my_tesla.battery.get_range()

print("\n-- Upgraded Battery --")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()