
n = 10
a, b = 0, 1
fibonacci_series = []

for i in range(n):
    fibonacci_series.append(a)
    a, b = b, a+b
    
print(fibonacci_series)


print("-----------------------------------")

number = int(input("Enter the number:"))

convert_number = int(str(number)[::-1])

if convert_number == number:
    print(f"The {number} is palimdrome number")
else:
    print(f"The {number} is not palimdrone number")
    
print("-----------------------------------")

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling inside the decorator")
        func(*args, **kwargs)
        print("DIIIIIDDDDDD")
    return wrapper


@decorator
def addtion(name):
    print(f"Hello {name}")
addtion("Dinanath")

print("-----------------------------------")

a=(10) 
b=(i for i in range(10)) 
print(type(a))
print(type(b))
print(0.0==0)

print("-----------------------------------")

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
set_num = list(set(nums))
print(set_num)
print("-----------------------------------")
student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

student["first name "] = student["name"]
del student["name"]

student["age"] = 21

student["email"] = "amit@example.com"

print(student)
print("-----------------------------------")

students = {
    "Amit": {"math": 80, "science": 75},
    "Tanvi": {"math": 90, "science": 85},
    "Rahul": {"math": 70, "science": 65}
}

# 1. Loop and print student name and total marks
for key, value in students.items():
    print(key)
    print(value["math"]+value["science"])

# 2. Add new student Neha
students["Neha"] = {"math": 60, "science": 76}

# 3. Update Tanvi's science mark to 88
students["Tanvi"]["science"] = 88

print(students)

print("-----------------------------------")

students = [
    {"name": "Amit", "math": 80, "science": 75},
    {"name": "Tanvi", "math": 90, "science": 88},
    {"name": "Rahul", "math": 70, "science": 65}
]

# 1. Print each name and total marks
for student_details in students:
    total_marks = student_details["math"]+student_details["science"]
    print(f"{student_details["name"]} scores total marks as {total_marks}")


# 2. Add Neha
students.append({"name": "Neha", "math": 95, "science": 90})

# 3. Print students with total marks > 170
for student_details in students:
    total_marks = student_details["math"]+student_details["science"]
    if total_marks>170:
        print(total_marks)
        
print(students)


























    



    
    
    
    
    
    
    