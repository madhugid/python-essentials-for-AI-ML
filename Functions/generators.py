

https://docs.python.org/3/tutorial/classes.html#generators# Generators
#  are functions that lazily produce a sequence of values using the yield keyword instead of returning values all at once like regular functions. This allows for lightweight lazy evaluation.

# Key Points

# Generators use yield to output values one by one, suspending and resuming execution between each value

# Generators automatically save state between executions

# Anything you can do with generators can be done with class-based iterators, but generators are more compact

# Generator expressions provide a short syntax similar to list comprehensions

# Reflection Questions

# When would you want to use a generator function instead of a normal function?

# What are some real-world examples where a generator would be useful?

# How do generators save state between executions?

# What happens if you reach the end of a generator function?

# What is the main syntactic difference between a generator function and normal function?

# Challenges

# Write a basic generator function that produces the numbers from 1 to 10

# Create a generator that produces the Fibonacci sequence infinitely

# Use a generator expression to calculate the sum of squares from 1 to 100

# Implement a generator that takes a list and loops over it in reverse order

# Build a random number generator using Python's random library and generator pattern

# https://docs.python.org/3/tutorial/classes.html#generators

def lazy_return_random_attacks():
    """Yield attacks each time"""
    
    # Import random library
    import random
    
    # Dictionary of attacks mapped to body part
    attacks = {"kimura": "upper_body", 
               "straight_ankle_lock":"lower_body",
               "arm_triangle":"upper_body",
               "keylock": "upper_body",
               "knee_bar": "lower_body"}

    # Infinite loop 
    while True:
        # Get random attack 
        random_attack = random.choices(list(attacks.keys()))
        
        # Yield attack one at a time
        yield random_attack
        
# Create attack generator 
attack = lazy_return_random_attacks()

# Show it's a generator object
print(type(attack)) 

# Print 6 random attacks
for _ in range(6): 
    print(next(attack))
