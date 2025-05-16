# sum of first n natural number using while statements

n = 10
sum = 0
count = 1

while count <= n:
    sum = sum + count
    count = count + 1
    
print("Sum of the natural number is", sum)

sum = 0
n = 10
for i in range(11):
    sum = sum + i
    
print(sum)