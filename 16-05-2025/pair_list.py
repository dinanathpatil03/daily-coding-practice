# pairing two list 

list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]

output = []

for i in list1:
    for j in list2:
        if i>0:
            z = [i, j]
            output.append(z)
print(output)

# by list comprehensive

pair = [[i, j]for i in list1 for j in list2]
print("Pair", pair)