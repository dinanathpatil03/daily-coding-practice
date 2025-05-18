## file handling and exception handling

try:
    file = open("example1.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File does not exist")

finally:
    if "file" in locals() or not file.closed():
        file.close()
        print("File closed")
