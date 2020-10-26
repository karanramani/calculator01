# Program make a simple calculator
import math
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function squares one number
def square(x):
    return x ** 2

# This function provides squareroot answer of one number
def sqrt(x):
    return math.sqrt(x)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print ("6.Square Root")
while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Check if choice is one of the four options
    if choice in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice in (5, 6):
        num1 = float(input("Enter a number: "))

        if choice == 5:
            print("Square of ", num1, "=", square(num1))
        elif choice == 6:
            print("Square root of ", num1, "=", sqrt(num1))

        break

    else:
        print("Invalid Input")