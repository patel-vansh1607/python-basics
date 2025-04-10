"""
= Dictionaries store data in key-value pairs
      Properties:
        * Key-Value Pairs
        * Unordered ( but insertion is ordered in python 3.7+ ) 
        * Mutable
"""

student_name = {
    "name": "Vansh",
    "age": 17,
    "city": "Mumbai"
}
#ACCESING
student_name["name"] #Vansh
#ADDING/UPDATING
student_name["city"] = "Nakuru"
#DELETING
del student_name["age"]
#LOOPING
for key, value in student_name.items():
    print(key, value)
# KEYS & VALUES
student_name.keys()
student_name.values()
# NESTING
students = {
    "student_1": {
        "name": "Vansh",
        "age": 17,
        "city": "Mumbai"
    },
    "student_2": {
        "name": "Saleh",
        "age": 19,
        "city": "Nakuru"
    }
}


user_name = {
    "email": "pvansh830@gmail.com",
    "phone_number": "0748660944",
    "password": "1234567890"
}
user_name["phone_number"] = "0700000000"
user_name["password"] = "0987654321"

company = {
    "company_1": {
        "name": "XYZ",
        "location": "YZX",
        "username": "@xyz"
    },
    "company_2": {
        "name": "ABC",
        "location": "CBA",
        "username": "@abc"
    }
}

