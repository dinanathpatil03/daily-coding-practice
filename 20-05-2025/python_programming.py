# write a program to calculate the sqaure of number

num = float(input("Enter the number:" ))
if num>0:
    sqaure = num*num
    print("The Square of number is:", sqaure)

# write the program to check weather number is even or odd

number = float(input("Enter the number: "))
if number == 0:
    print("The number is neither even or odd")
elif number%2 == 0:
    print("The number is Even number")
else:
    print("The number is odd number")

# write the code to find the sum of the first n natural number

n = int(input("Enter the natural number: "))
sum_n = (n * (n+1)) // 2
print(f"The sum of n natural number is {sum_n}")

# write a program to check weather the year is leap year.

year = int(input("Enter the year: "))
if (year%4==0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year.")

# write a program reverse the string

string1 = str(input("Enter the string: "))
reverse = string1[::-1]
print(f"The reverse string is given {reverse}")


