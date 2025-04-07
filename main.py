#DATA TYPES IN PYTHON
"""
# 1. Numeric Types
#    - int: Integer values (e.g., 5, -3, 42)   
#    - float: Floating-point numbers (e.g., 3.14, -0.001, 2.0)
#    - complex: Complex numbers (e.g., 2 + 3j, -1 - 1j)
"""
x = 1.2
y = 1
cp = 2 + 3j

#Strings
msg = "Hello"

#Boolean
t = True
f = False


#Collection Data Types
#Mutable - values can be changed in place
#Immutables - cannot be changed after creation(you get a new object)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Tuples (Ordered, Mutable)
coords = (10,20)

#Dictonary (Key:Value pairs, Mutable)
person = {"name": "Vansh", "age": 17}

#Sets (Unordered, Unique elements)
colors = {"red", "green", "blue"}
colors.add("yellow")

#Type Conversion
#Converting from one data type to another 
#Converting int to str
num = 100.12
numStr = str(num) # "100.12"

#Converting str to int
numInt = int(numStr) # 100.12

#Converting str to float
numFloat = float(numStr) # 100.12

print(numInt)

