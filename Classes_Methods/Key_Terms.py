# Key Terms
# Class: Blueprint for creating objects. Defines attributes and methods.

# Instance: Object that is created from a class. Has access to class attributes and methods.

# Method: Function that belongs to a class. Accessed via instance or class name.

# Constructor: Special method that runs when an instance is created. Used to initialize attributes.

# Inheritance: Creating a child class from parent class. Child inherits attributes and methods.

# Class Example
class Vehicle:
    wheels = 4 # Class attribute
    
    def __init__(self, make, model):
        self.make = make # Instance attribute
        self.model = model
        
    def description(self): # Method
        return f"The {self.make} {self.model}"

car = Vehicle("BMW", "i3") # Instance created
print(car.wheels) # Access class attribute
print(car.description()) # Call instance method

# Inheritance Example
class Pet:
    def eat(self):
        print("Chomp")
        
class Dog(Pet):
    def bark(self):
        print("Bark!")
        
dog = Dog()
dog.eat() # Inherited method
dog.bark() # Dog specific method
