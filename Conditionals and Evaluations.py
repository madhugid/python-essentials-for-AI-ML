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

if has_kids and married:
    print("This person is married and has kids.")

# Using not with conditions
is_logged_in = False
likes_books = False

if not likes_books and not is_logged_in:
    print("User not logged in.")
