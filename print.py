name = "Alan"
age = 20
address = "Kathmandu"
#formatted-string method
print(f"My name is {name} and I am {age} years old and address is {address}.")
#concatenation method - only supports similar data types like here even age is changed to string
print("My name is " + name + " I am " + str(age) +" years old." + " address is " + address + ".")

# Format Method [2- types]

#%formatting legacy[old] method
print("My name is %s and age is %d and address is %s."%(name,age,address))
"""Format Specifiers(used here)
%s - strings
%d - integers"""

#.format() method - modern method
print("My name is {0} and age is {1} and address is {2}.".format(name,age,address))

#for single line comment

"""For
multi-line 
comment"""