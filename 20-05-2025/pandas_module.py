import pandas as pd

# Creating a Series that is one dimentional array object
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series \n", series)

# Create series from dictionary
dictionary = {"a":1, "b":2,"c":3}
series1 = pd.Series(dictionary)
print(series1)

# create dataframe 
dictionary = {
        "Name": ["Dinanath", "Aditi", "Mahesh"],
        "Age": [27, 23, 27],
        "City": ["Paithan", "Karve nagar", "Kondhwa"]

    }
data_frame = pd.DataFrame(dictionary)
print("Data frame\n", data_frame)

# create dataframe by different variables
dict1 = {
    "name" : ["Dinanath", "Shrihari", "Yash", "Mahesh", "Shubham", "Nitin", "Rajat"],
    "job_profile" : ["Engineer", "Trainer", "Boxer", "Developer", "Designer", "Engineer", "Trainer"],
    "Age": [27, 26, 26, 27, 27, 28, 26],
    "Marrital Status": ["Single", "Single", "Single+Engage", "Single", "Engage", "Engage", "Engage"]
}

data_frame = pd.DataFrame(dict1)
print("Friends and their job\n", data_frame)

# create dataframe with list

list1 = [
    {"name":"Dinanath", "age":27, "City":"Paithan"},
    {"name":"Aditi", "age":23, "City":"Paithan",},
    {"name":"Bhargavi", "age":18, "City":"Sambhajinagar"},
    {"name":"Atharv", "age":22, "City":"Sambhajinagar",}
]
data_frame = pd.DataFrame(list1)
print("Data Frame for family\n", data_frame)

