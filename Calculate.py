# Simple Calculator
def add():
    additon=first_number+second_number
    print(additon)
def subtract():
    subtraction=first_number-second_number
    print(subtraction)

def times():
    multiplication=first_number*second_number
    print(multiplication)
def divide():
    division=first_number/second_number
    print(division)

print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    add()

elif operation == "subtract":
    subtract()

elif operation == "multiply":
   times()

elif operation == "divide":
   divide()
else:
    print("Sorry, I do not understand your request.")
