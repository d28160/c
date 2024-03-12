import re

email_cond = "^[a-z]+\w+[@]+\w+[.][a-z]{2,3}$"
user_email = input("Enter your email :- ")

if re.search(email_cond, user_email):
    print("Right email.")
else:
    print("Wrong email.")