# STRINGS
"""
= Python offers a variety of built-in string methods for manipulating strings.
"""
message = "Hello, greetings fromt Rift Koders, We are busy typing code "
message.lower() # Converts to lowercase
message.upper() # Converts to uppercase
message.split(",") # splits by comma
# CHECKING CONTENT
print("greetings" in message) 
prints(message.startswith("Hello")) 
# STRIPPING WHITESPACE
msg = "   Hello   "
msg.strip()
# REPLACE
message.replace("Hello", "Yellow") 
# COUNT AND FIND
message.count("are")
message.find("code")
#STRING FORMATTING
name = "Vansh"
print(f"Hello {name}") 