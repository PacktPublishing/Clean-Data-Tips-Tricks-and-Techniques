from nltk.tokenize import word_tokenize

with open("shakespeare.txt", "rb") as f:
    content = f.read().decode('utf-8')
    tokens = word_tokenize(content)
    print(tokens)
