n = int(input("Enter the input value: "))
a, b = 0, 1

fibonacci_series = []

for i in range(n+1):
    fibonacci_series.append(a)
    a, b = b, a + b

print(f"Fibonacci series is {fibonacci_series}")