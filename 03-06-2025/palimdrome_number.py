
number = 12321

rev = int(str(number)[::-1])

if number == rev:
    print("The number is palimdrome ")
else:
    print("Not palimdrome")
   
## THis both are the approches for palimdrome number
## separated by the comment

user_inp = input("Enter the number: ")

cleaned_input = user_inp.replace(" ", "").lower()

if cleaned_input == cleaned_input[::-1]:
    print(f"The {user_inp} is palimdrome number")
else:
    print(f"The {user_inp} is not palimdrome")