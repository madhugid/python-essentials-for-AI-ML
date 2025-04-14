Class: Defines a template
# Class 
class UFC:  
    pass

# Object: An instance of a class
# Class 
class UFC:  
    pass

# Object
ufc = UFC()

# Attribute: Variables bound to an object
class Fighter:
    def __init__(self):
        self.name = "Conor McGregor"  # Attribute 

fighter = Fighter()
print(fighter.name)

# Method: Functions defined in a class

class Fighter:
    def trash_talk(self):# Method
        print("I'm the best!")

fighter = Fighter()
fighter.trash_talk()

# Inheritance: Child class inherits from parent class

class Athlete:
    pass

class Fighter(Athlete):# Inheritance 
    pass

# Python Code Example:  Simple Inheritance
# Create a simple Competitor class
class Competitor:

  def __init__(self, name, age, weight):
    self.name = name 
    self.age = age
    self.weight = weight
 
 # Method Prints competitors stats           
  def print_stats(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight} pounds.")

# Create a Fighter class that inherits from Competitor
class Fighter(Competitor):
  pass

fighter = Fighter("Conor McGregor", 32, 170) 
fighter.print_stats()


# Python Code Example:  Using Inheritance
# Example using inheritance 

class UFC:

  def weight_class(self, weight):
      # Maps weight to weight class
      return "Lightweight"  

# Fighter class inherits from UFC
class Fighter(UFC):

  def __init__(self, name):
    self.name = name
  
  def print_name(self):
    print(self.name)

fighter = Fighter("Khabib")  
print(fighter.weight_class(155)) 
fighter.print_name()
