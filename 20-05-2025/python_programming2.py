# write a program that prints 5*5 grid of asterisks(*) using nested loops

for i in range(6, 0, -1):
    for j in range(0, i-1):
        print("*", end="")
    print()

# write a program that asks user to input numbers until they input 0. THE program should print the sum of all the numbers entered by the user.
input_num = int(input("Enter the number: "))
sum = 0
while input_num != 0:
    sum = sum + input_num
    input_num = int(input("Enter the number: "))
print("The sum of the number is", sum)

# write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# write a program that defines an empty function using pass statement
def empty_function():
    pass

empty_function()

# 