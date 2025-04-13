# Python Exceptions Example

# Example 1: ZeroDivisionError
# This example demonstrates what happens when you try to divide by zero.
try:
    result = 14 / 0
except ZeroDivisionError as e:
    print(f"Got an error: {e}")  # This will print the error message for division by zero.

# Example 2: Raising a RuntimeError
# Here we explicitly raise a RuntimeError with a custom message.
raise RuntimeError("This is a problem")  # This will stop the program and show the error.

# Example 3: Catching Specific Exceptions
# This example shows how to catch specific exceptions.
try:
    result = 14 / 0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError, performing a different operation.")
    result = 14 / 2  # This will execute if the above line raises an error.
    print(f"Result is: {result}")

# Example 4: Catching Multiple Exceptions
# This example demonstrates how to catch multiple exceptions.
try:
    result = 14 / 0
    result += "string"  # This will cause a TypeError.
except (ZeroDivisionError, TypeError) as e:
    print(f"Caught an error: {e}")

# Example 5: Assigning Exception to a Variable
# This example shows how to assign the exception to a variable for further use.
try:
    result = 14 / 0
except ZeroDivisionError as error:
    print(f"Got an error: {error}")  # This will print the error message.
