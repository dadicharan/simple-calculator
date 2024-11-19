import math
import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def factorial(n):
    if n < 0:
        return "Error! Factorial of a negative number doesn't exist."
    return math.factorial(int(n))

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def logarithm(a):
    if a <= 0:
        return "Error! Logarithm of zero or negative number is undefined."
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        return "Error! Natural log of zero or negative number is undefined."
    return math.log(a)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    history = []
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Factorial")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Logarithm (base 10)")
        print("12. Natural Logarithm")
        print("13. View History")
        print("14. Clear Screen")
        print("15. Exit")
        
        choice = input("Enter choice (1-15): ")
        
        if choice == '15':
            print("Exiting the calculator. Goodbye!")
            break

        elif choice == '14':
            clear_screen()
            continue

        elif choice == '13':
            if history:
                print("\nCalculation History:")
                for h in history:
                    print(h)
            else:
                print("No calculations yet!")
            continue

        elif choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            elif choice == '6':
                result = modulus(num1, num2)
            print(f"The result is: {result}")
            history.append(f"{num1} {choice} {num2} = {result}")

        elif choice == '7':
            num = float(input("Enter a number for factorial: "))
            result = factorial(num)
            print(f"The result is: {result}")
            history.append(f"{num}! = {result}")

        elif choice in ['8', '9', '10']:
            num = float(input("Enter the angle in degrees: "))
            if choice == '8':
                result = sine(num)
            elif choice == '9':
                result = cosine(num)
            elif choice == '10':
                result = tangent(num)
            print(f"The result is: {result}")
            history.append(f"{choice}({num}) = {result}")

        elif choice in ['11', '12']:
            num = float(input("Enter a number: "))
            if choice == '11':
                result = logarithm(num)
            elif choice == '12':
                result = natural_log(num)
            print(f"The result is: {result}")
            history.append(f"{choice}({num}) = {result}")

        else:
            print("Invalid input. Please try again.")

# Run the calculator
calculator()
