from nltk import skipgrams

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import itertools

stopwords = list(stopwords.words('english'))
numbers = list(range(0, 100))  # number that are identifiers of pages
forumSpecificWords = ['>', '<', '?', '[', ']'] + numbers  # special signs
stopwords += forumSpecificWords

with open("shakespeare.txt", "rb") as f:
    content = f.read().decode('utf-8')
    tokens = word_tokenize(content)
    withoutStopWords = [w for w in tokens if not w in stopwords]

for w in tokens:
    if w not in stopwords:
        withoutStopWords.append(w.strip())  # clean whitespaces

print("\n---2,2:", list(skipgrams(itertools.islice(withoutStopWords, 100), 2, 2)))
print("\n---2,3:", list(skipgrams(itertools.islice(withoutStopWords, 100), 2, 3)))
print("\n---3,2:", list(skipgrams(itertools.islice(withoutStopWords, 100), 3, 2)))
