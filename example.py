#print try some of these key terms out
# Variable to store a value
name = "John"  

# Reassign variable
name = "Jane" 

# f-String prints variable 
print(f"Hello {name}")

# Integer
num = 10  

# Float 
dec = 10.5 

# Boolean
is_true = True

# None 
empty = None

# If condition evaluates the Boolean
if is_true:
  print("Condition was true")

# Else catches when if was False  
else: 
  print("Condition was false")
  
# Try block attempts this code
try:
  result = num / 0
# Except catches the ZeroDivisionError   
except ZeroDivisionError as e:
  print("Cannot divide by 0")
