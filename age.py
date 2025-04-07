age = int(input("Enter your age : "))

if age <= 13:
    print("You are a child.")
elif age >= 14 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 64:
    print("You are an adult.")
else:
    print("Invalid age entered.")
print("Thank you for using the age classification program!")