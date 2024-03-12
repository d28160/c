import tokenize

with tokenize.open("1a.py") as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
