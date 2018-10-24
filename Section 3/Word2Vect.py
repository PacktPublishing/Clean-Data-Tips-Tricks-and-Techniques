from gensim.test.utils import common_texts
from gensim.models import Word2Vec

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

model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
inputTooMLModel = model.train(itertools.islice(withoutStopWords, 10_000), total_examples=len(withoutStopWords), epochs=1)
print(inputTooMLModel)
