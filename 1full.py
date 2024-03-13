
my_text = input("Enter a String for tokenization: ")
my_token = my_text.split()
print("Tokenization of given input:")
print(my_token)


import tokenize

with tokenize.open("1a.py") as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)


import re
my_text = input("Enter a string for tokenizate :- ")

print("Tokenization of given input :- ")
pattern = re.compile("\w+")
matches = pattern.finditer(my_text)

for token in matches:
    print(token)