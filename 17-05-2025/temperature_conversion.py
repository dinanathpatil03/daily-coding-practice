# temperature conversion

def templerature_conversion(temp, unit):
    if unit == "C":
        return temp * 9/5 + 32
    elif unit == "F":
        return (temp-32) * 5/9
    else:
        None
print(templerature_conversion(25, "C"))   
print(templerature_conversion(77, "F"))