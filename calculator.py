import math

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

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Factorial")
        print("8. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
        
        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {power(num1, num2)}")
            elif choice == '6':
                print(f"The result is: {modulus(num1, num2)}")
        elif choice == '7':
            num = float(input("Enter a number for factorial: "))
            print(f"The result is: {factorial(num)}")
        else:
            print("Invalid input. Please try again.")

# Run the calculator
calculator()
