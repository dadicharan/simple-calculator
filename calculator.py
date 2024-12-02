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

def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not real."
    return math.sqrt(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def sinh(a):
    return math.sinh(a)

def cosh(a):
    return math.cosh(a)

def tanh(a):
    return math.tanh(a)

def logarithm(a):
    if a <= 0:
        return "Error! Logarithm of zero or negative number is undefined."
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        return "Error! Natural log of zero or negative number is undefined."
    return math.log(a)

def radians_to_degrees(r):
    return math.degrees(r)

def degrees_to_radians(d):
    return math.radians(d)

def percentage(part, whole):
    if whole == 0:
        return "Error! Percentage calculation with a zero denominator."
    return (part / whole) * 100

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
        print("8. Square Root")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("12. Hyperbolic Sine")
        print("13. Hyperbolic Cosine")
        print("14. Hyperbolic Tangent")
        print("15. Logarithm (base 10)")
        print("16. Natural Logarithm")
        print("17. Radians to Degrees")
        print("18. Degrees to Radians")
        print("19. Percentage")
        print("20. View History")
        print("21. Clear Screen")
        print("22. Exit")
        
        choice = input("Enter choice (1-22): ")
        
        if choice == '22':
            print("Exiting the calculator. Goodbye!")
            break

        elif choice == '21':
            clear_screen()
            continue

        elif choice == '20':
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
