import re

number = input("Enter your phone number?")

if re.search(r"^07+\d{9}$", number):
    print("Valid")

else:
    print("Invalid")