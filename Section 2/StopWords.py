from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))
print('All tokens in a English alphabet', stopwords)

with open("shakespeare.txt", "rb") as f:
    content = f.read().decode('utf-8')
    tokens = word_tokenize(content)
    withoutStopWords = [w for w in tokens if not w in stopwords]

for w in tokens:
    if w not in stopwords:
        withoutStopWords.append(w)

print(withoutStopWords)
