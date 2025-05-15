# Calculator

num1 = float(input("Enter the number1: "))
num2 = float(input("Enter the number2: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Entered operation is not present")
    
print("Result:" , result)