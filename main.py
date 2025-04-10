# DATA TYPES IN PYTHON
"""
# 1. Numeric Types
#    - int: Integer values (e.g., 5, -3, 42)   
#    - float: Floating-point numbers (e.g., 3.14, -0.001, 2.0)
#    - complex: Complex numbers (e.g., 2 + 3j, -1 - 1j)
"""
x = 1.2
y = 1
cp = 2 + 3j

# Strings
msg = "Hello"

# Boolean
t = True
f = False


# Collection Data Types
# Mutable - values can be changed in place
# Immutables - cannot be changed after creation(you get a new object)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Tuples (Ordered, Mutable)
coords = (10,20)

# Dictonary (Key:Value pairs, Mutable)
person = {"name": "Vansh", "age": 17}

# Sets (Unordered, Unique elements)
colors = {"red", "green", "blue"}
colors.add("yellow")

# Type Conversion
# Converting from one data type to another 
# Converting int to str
num = 100.12
numStr = str(num) # "100.12"

# Converting str to int
numInt = int(numStr) # 100.12

# Converting str to float
numFloat = float(numStr) # 100.12

print(numInt)

# CONTROL FLOW
"""
CONTROL FLOWS REFERS TO THE ORDER IN WHICH INDIVIDUAL STATMENTS, INSTRUCTIONS OR FUNCTION CALLS ARE EXECUTED OR EVALUATED.
YOU CAN CONTROL FLOW USING:
"""

# CONDITIONAL STATEMENTS

"""
CONDITIONAL STATEMENTS IN PYTHON ALLOW YOU TO EXECUTE BLOCKS OF CODE BASED ON CERTAIN CONDITIONS.
"""

# if ...  elif ... else

if True:
    print("This will execute")
elif False:
    print("This will print")
else:
    print("This is the last part to exceute")

# LOOPS

"""
THEY ARE USED TO ITERATE OVER A SEQUENCE OF ELEMENTS OR EXECUTE A BLOCK OF CODE REPEATEDLY.
"""

# FOR LOOP
# USED TO ITERATE OVER SEQUENCES (LIKE LISTS, STRINGS, RANGES)
for i in range (1,11):
    print(i)
# WHILE LOOP
# RUNS AS LONG AS THE CONDITION IS TRUE
count = 0
while count < 5: # CONDITION
    print("Count is ", count)
    count += 1

# FUNCTIONS

"""
THEY ALLOW YOU TO ENCAPSULATE REUSABLE PEICES OF CODE AND ENHANCE CODE MODULARITY.
"""
def add_sum(a,b):
    return a + b
result = add_sum(10, 20)
print(result)


# WHY DATA STRUCTURES MATTER

"""
= They organize, store and manage data in ways that make your program more efficient, readable, and powerful.
= Diffrent problems need diffrent way to store and retrieve data.
= Lists are a great way for ordered collection you change .
= Tuples are like lists but immutable, perfect for mixed data.
= Dictionaries gives you fast access to data using keys.
= Using the right data structures makes your code faster.
= Looking up at an item in a dictionary is much faster thab a searching list.
= A set is great when you want to remove duplicates.
= Well chosen data structures make code easier to understand
    e.g 
    instead of:-
            names = ["Tilak", "Ansh", "Esha"]
            ages = ["18", "18", "20"]
        We can do this:
            students = {"Tilak" : 18,"Ansh" : 18,"Esha" : 20}
"""