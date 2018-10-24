import numpy
from collections import Counter

n = numpy.array([1, 1, 2, 3, 3, 3, 0])
print("original", n)

print("most common:", Counter(n).most_common())

res = [x[1] for x in Counter(n).most_common() if x[0] > 1]

print("Duplicates: ", res)
