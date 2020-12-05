import math
import csv
import unittest

# Calculator Class defined

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

# Square
def square(x):
    return x ** 2

# Squareroot
def sqrt(x):
    return math.sqrt(x)


# Program Start
print("Select operation.")

while True:
    mode = int(input("Please Enter 1 for CALCULATOR mode OR 2 to perform UNIT TESTS: "))

# Calculator Section

    if mode == 1:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print ("6. Square Root")
        choice = input("Enter choice from above: ")
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

        else:
            print("Invalid Input")

# Unit Test section

    elif mode == 2:
        print ("1. Run Test Addition")
        print ("2. Run Test Subtraction")
        print ("3. Run Test Multiplication")
        print ("4. Run Test Division")
        print ("5. Run Test Square")
        print ("6. Run Test Square Root")
        print ("7. Run String Test")
        choice = input("Enter choice from above: ")

        if choice in (1,2,3,4,5,6,7):
            if choice == 1:
                with open('Test-scripts/Unit Test Addition.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 2:
                with open('Test-scripts/Unit Test Subtraction.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 3:
                with open('Test-scripts/Unit Test Multiplication.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 4:
                with open('Test-scripts/Unit Test Division.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 5:
                with open('Test-scripts/Unit Test Square.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 6:
                with open('Test-scripts/Unit Test Square Root.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif choice == 7:
                with open('Test-scripts/Unit Test String Test.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            else:
                print("Invalid Input")
    continue


