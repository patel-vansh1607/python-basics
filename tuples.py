# TUPLES
"""
= Tuples are similar to lists but immutable ( cannot change ) once created.
    Properties:
        * Ordered
        * Immutable
        * Faster than lists
        * Good for fixed data
"""
names = ("Saleh", "Vansh", "Ansh", "Tilak", "Esha")
#  INDEXING
names[0] #Saleh
# TUPLE UNPACKING
a,b,c,d,e = names
print(a) # Saleh

"""
Where to use:
    * Coordinates
    * Function return value
"""


movies = ("Inception", "Interstellar", "The Dark Knight", "URI", "RRR")
movies[1] = "SUI"  # CANT WORK BECAUSE TUPLE IS MUTABLE
print(movies) 




