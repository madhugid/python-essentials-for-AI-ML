# Function: A reusable block of code that performs a specific task. Defined using the def keyword.

# Arguments: Values passed into a function when calling it. Allows customizing behavior.

# Variable Arguments: Allows passing an arbitrary number of arguments to a function.

# Keyword Arguments: Arguments passed by name rather than position. Can have default values.

def double(x):
    """Doubles a number"""
    return x * 2

print(double(5)) # Prints 10


# Function with Arguments
def full_name(first, last):
    return first + " " + last

print(full_name("John", "Doe")) # Prints John Doe

# Variable Arguments
def sum_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(sum_all(1, 2, 3)) # Prints 6

# Keyword Arguments
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)

greet("John") # Prints Hello, John
greet("Mary", greeting="Hi") # Prints Hi, Mary

# Generator: A type of iterable like lists or tuples but does not store the full sequence in memory at once. Uses yield to generate one item at a time
#counter generator
def counter(start=0):
    n = start
    while True:
       yield n
       n += 1

for i in counter(5):
    if i > 10:
        break 
    print(i)

#Infinite Fibonacci sequence generator
def fib():
    a, b = 0, 1
    while True:
       yield a 
       a, b = b, a + b
       
for n in fib():
   if n > 10:
     break  
   print(n)


# Generator expression: More compact syntax like list comprehensions for inline lazy generation, uses () instead of []
#Generator expression to get squares
nums = (x**2 for x in range(10))
print(list(nums))

Infinite sequence: Generators can be infinitely recursive/iterative to model data streams
# Infinite random attack sequence
import random

attacks = ["kimura", "armbar", "triangle"] 

def lazy_random_attacks():
    """Lazily yield random attacks forever"""
    
    while True:
        attack = random.choice(attacks)
        print("Yielding attack") 
        yield attack
        
generator = lazy_random_attacks()

for _ in range(5):
    print(next(generator))
