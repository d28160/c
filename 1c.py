import re
my_text = input("Enter a string for tokenizate :- ")

print("Tokenization of given input :- ")
pattern = re.compile("\w+")
matches = pattern.finditer(my_text)

for token in matches:
    print(token)