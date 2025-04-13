# Example of using if, elif, and else statements

# Variables
properties = 0
parents = 2
name = None
last_name = None

# If statement
if properties > 0:
    print("We have properties.")
else:
    print("We have no properties.")

# Elif statement
if properties == 0:
    if parents > 0:
        print("We have parents.")
    else:
        print("We have no parents.")

# Checking for None
if not name:
    print("Didn't get a name.")

if not last_name:
    print("Didn't get a last name.")

# Compound conditions
has_kids = True
married = True




# Example 1: Basic if statement
condition = True
if condition:
    print("The condition was met.")

# Example 2: If condition evaluates to false
condition = False
if condition:
    print("This will not print.")

# Example 3: Truthiness of data structures
groceries = []
if groceries:
    print("We have some groceries.")
else:
    print("We don't have any groceries.")

invites = ["Alice", "Bob"]
if invites:
    print("We have some invites.")

# Example 4: Evaluating integers
properties = 0
if properties:
    print("We have properties.")
else:
    print("We have no properties.")

parents = 2
if parents > 1:
    print("There is more than one parent.")

# Example 5: Using else
if properties > 0:
    print("We have properties.")
else:
    print("We have no properties.")

# Example 6: Using elif
if properties > 0:
    print("We have properties.")
elif parents > 0:
    print("We have parents.")
else:
    print("We have neither properties nor parents.")

# Example 7: Using not with conditions
name = None
if not name:
    print("Didn't get a name.")

last_name = None
if not last_name:
    print("Didn't get a last name.")

# Example 8: Compound conditions
has_kids = True
married = True
if has_kids and married:
    print("This person is married and has kids.")

# Example 9: Using not with compound conditions
is_logged_in = False
likes_books = False
if not likes_books and not is_logged_in:
    print("User not logged in.")
if has_kids and married:
    print("This person is married and has kids.")

# Using not with conditions
is_logged_in = False
likes_books = False

if not likes_books and not is_logged_in:
    print("User not logged in.")
