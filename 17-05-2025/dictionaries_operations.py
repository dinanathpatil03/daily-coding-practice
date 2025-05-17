# nested dictionary

students = {
    "student1" : {"name": "Dinanath", "age": 27},
    "student2" : {"name": "Shrihari", "age": 26}
}

for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key, value in student_info.items():
        print(f"{key}:{value}")


# dictionary comprehension
# sqaure the values

dictionary = {}

for x in range(10):
    dictionary.update({x:x**2})
print(dictionary)

comprehensive_dict = {x:x**2 for x in range(5)}
print("comprehensive_dict", comprehensive_dict)

# use dictionary to count the frequency of elements of list

numbers = [1,1,1,1,2,3,2,2,3,3,3,3,3]
dic = {}

for x in numbers:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
print(dic)

# merging two dict

dict1 = {"a":1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}
print("merged_dict", merged_dict)