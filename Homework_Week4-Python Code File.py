#
# Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.

from datetime import datetime

# Get current date and time
DateTime_Now = datetime.now()

# Extract the full month name
month_name = DateTime_Now.strftime("%B")
print("Current month:", month_name)


# Write a simple function that takes 2 parameters -- a first name and a day name.

    #    Set a default value for the day name of Sunday.
    #    Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.
    #    Invoke this function with 2 variables.
    #    Invoke this function with 1 variable only.


def greet(first_name, day_name="Sunday"):
    print(f"Hi {first_name}! Happy {day_name}!")

# Invoke the function with 2 variables
greet("Eddie", "Monday")

# Invoke the function with 1 variable only
greet("Fred")

# Write a block of code to handle one of the most common Python exception errors. 
# Select one of the common errors from the curriculum section on Python Exception handling. Have your code example uses the try,except, else, and finally components.

try:
    # Attempt division by zero
    result = 15 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
else:
    print("Division successful. Result:", result)
finally:
    print("Execution of the try-except block is complete.")

try:
    # Attempt division by zero
    result = 15 / 5
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
else:
    print("Division successful. Result:", result)
finally:
    print("Execution of the try-except block is complete.")
