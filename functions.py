# FUNCTIONS

"""
= A function is a reusable block of code that performs a specific task.
= Functions can take parameters (inputs) to work with data and can return values (outputs) to provide results.
= Functions in python are defined using the def keyword and can take parameters.
"""
def greet(name):
    return f"Hello, {Vansh}!"
greet("Vansh")

"""
= Parameters are variables listed in the function defination that act as placeholder for the values (arguments) 
passed to the function when it is called.
= Return value is the value a function sends back to the caller using the return statement, if no return statement is 
specified, the function returns None by default
"""
def add_sum(a, b): #parameters a and b
    result = a + b
    return result # results the sum of a and b
#calling the function
add_sum(10, 20) #arguments 10 and 20
"""
= above
    * a,b are parameters
    * 10,12 are arguments (actual values passed to the function)
= The function returns result which stores the sun of  a and b
"""

# DEFAULT PARAMETERS
def greetUser(name="Guest") # default parameter value set to name variable
    print(f"Greetings {name}")
greetUser() # Greetings, Guest
greetUser("Joseph") #Greetings Joseph

"""
= Functions can habve multiple return values, often as a tuple.
"""

def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder 
q, r = divide_and_remainder(10, 3)
print(q,r)

"""
= Parameters allow flexibility by letting functions work together with diffrent inputs.
= The return statement sends a value back, without it, the functions returns None.
= You can call a function anywhere in your code ( after defining it) and uses its return value.
"""

#FUNCTION SCOPE, GLOBAL VS LOCAL VARIABLES
"""
= Variables declared inside a function are local to that function.
= They exist within the function and are destroyed whewn the function finishes executing.
= They cannot be accessed outside the fucntion.
"""

def calculate_area(length, width):
    area = length * width # local variable area
    return area
print(calculate_area(10,12))
#print(area) # error "area" is not defined (it's local to the function)
#area is local and cannot be accessed outside the function
