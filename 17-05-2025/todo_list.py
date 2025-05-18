# To do list

to_do_list = ["Electricity bills", "Cleaning the house", "Buy Grocery"]

# Adding the task to list
to_do_list.append("Daily walking")
to_do_list.append("Go to guy")

# removing the task have been completed
to_do_list.remove("Cleaning the house")

# electricity bills are paid

if "Electricity bills" in to_do_list:
    print("Please pay the bills remaining")
    
print("Printing to do task has been remaining")
for task in to_do_list:
    print(f"-{task}")