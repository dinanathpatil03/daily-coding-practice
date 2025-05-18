# read the whole file

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

print("********************************************")

# read file by line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # removes the new line character

print("********************************************")

# writing a file
with open("example.txt", "w") as file:
    file.write("Hello World!!\n")
    file.write("This is new line.\n")
    
# write the new line without overwrite
with open("example.txt", "a") as file:
    file.write("Appending the new line.\n")