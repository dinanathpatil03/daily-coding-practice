## Input: s = "a0b1c2"
## Output: "0a1b2c"

s = "a0b1c2"
# s = "covid2019"
digits = []
letters = []

for i in s:
    if i.isalpha():
        #print("Alpha", i)
        letters.append(i)
    elif i.isdigit():
        #print("Digit", i)
        digits.append(i)
        
output = []

for d, l in zip(digits, letters):
    output.append(d)
    output.append(l)
    
result  = "".join(output)
print(result)