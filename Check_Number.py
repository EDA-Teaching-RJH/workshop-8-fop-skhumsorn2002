import re

number = input("Enter your phone number?")

if re.search(r"\d+^07+.{9}$", number):
    print("Valid")

else:
    print("Invalid")