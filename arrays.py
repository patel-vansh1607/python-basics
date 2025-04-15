# ARRAYS

"""
= Arrays are fundamental data structures that store elements in a contigous block of memory.
= Each element in an array is identified by an index, starting from 0.
= Arrays provide constant time access to any element using its index.

KEY CHARACTERTISTICS
= Arrays can have a fixed size or be dynamic.
= In strict arrays (Homogenous), all elements must be of the same type, in python's lists, they can store elements of 
diffrent types ( integers, strings, objects) i.e Hetrogenous.
= Elements are accessed using their index.
= Elements are stored next to each other in memory (Contigous Memory), aloowing fast access but potentially costly 
when re-sizing.
= List can grow or shrink as needed by using menthods like append() or pop().
= List have refrences to objects, not raw data, so they use more memory than traditional arrays.

HOW WE CAN IMPLEMENT ARRAYS IN PYHTON:
1. List: Dynamic, flexible and commonly used as array-like-structures.
2. Array Module: Provides a more traditional array with fixed type of elements.
3. Numpy Arrays: Specialized for numerical and scientific computing.
"""

#OPERATIONS ON LISTS

"""
= Arrays support a variety of operations that allow you to manipulate and access data stored within them.
"""

# INITIALIZATION
my_list = [] #empty list
my_list = [1,2,3,4] # list with initial elements

# ACCESSING ELEMENTS

"""
= Elements can be accessed by using the index, with a time complexity of 0(1)
"""
my_list[2] #3

# APPENDING ELEMENTS
my_list.append(6) # adding 6 to to the end of the list

#INSERTING ELEMENTS
"""
= Inserting elements can be done at the begining, end or any specified index in the array with the time complexity
of 0(n)/Linear Time for insertion at the begining or middle, 0(1)/Constant time fir insertion at the end(armotized)
"""

my_list.insert(1,1.3) # inserts 1.3 and index 1

# DELETING ELEMENTS
"""
= Deletion can be done from the begining, end or at any specified index in the array with a time complexity of 
0(n)/Linear Time for deletion from the begining or middle, 0(1)/Constant time for deletion from the end
"""
my_list.pop(1) # removes element at index i
my_list.pop() #removes last element of the array
# SLICING
my_list[1:3]

# TRAVERSING THE ARRAY/ITERATION
"""
= Traversing involves accesing each element of the array sequentially with a time complexity of 0(n)
"""
# TRAVERSING THE ARRAY/ITERATION
my_list = [1, 2, 3, 4, 5]  # example list

for element in my_list:
    print(element)  # accessing each element

# SEARCHING ELEMENTS
"""
= Searching the array can be done using linear search, or binary search
 ( if the array is sorted)
= Time ComplexityL 0(n) for linear search, 0(log n) for binary search
"""

# PYTHON ARRAY MODULE
"""
= The array module provides a closer implementation to traditional arrays, enforcing a single data type and using
less memory than lists
= It's used for scenarios requring compmact storage homegenous data like numerical processing.
"""

# CHARACTERISTICS OF PYTHON ARRAY MODULE
 """
 = Elements must be specific type, defined using type code.
 = Arrays are not truly fized but require manual rezizing.
 = It stores raw data, not object references, making it memory efficient.
 = It supports few operations than lists but it's optimized for basic array tasks,
 """

# TYPE CODES
"""
    'b' = signed char(1 byte)
    'i' = signed int(typically 4 bytes)
    'v' = float(4 bytes)
    'd' = double(8 byte)
"""

