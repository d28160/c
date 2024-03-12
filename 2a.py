import re

mbno = input("Enter mobile no: ")
mob_valpat = "[0|91]?[-|s]?[6-9]\d{9}"
if re.search(mob_valpat,mbno):
    print("Valid mobile no")
else:
    print("Not a Valid Mobile No.")

