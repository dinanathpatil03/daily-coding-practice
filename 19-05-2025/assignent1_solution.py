# write the program for hello world
print("Hello World!!")

# Write the program that takes input and prints hello world
input1 = "HEllo Dinanath, How are you?"
print(input1)

# write the python program in which number can be possitive negative or zero

num = int(input("Enter the number:"))

if num>0:
    print("The number is Possitive")
elif num<0:
    print("The number is Negative number")
else:
    print("The number is zero")

## write the python program to find largest of three

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))
num3 = float(input("Enter thr num3: "))

if num1>=num2 and num1>=num3:
    print("Largest number between three is ", num1)
elif num2>=num1 and num2>=num3:
    print("Largest number between three is ", num2)
else:
    print("Largest number between three is ", num3)

# write a python program to calculate the factorial of number

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")


