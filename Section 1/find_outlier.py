import numpy

arr = [-1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10000]

elements = numpy.array(arr)

mean = numpy.mean(elements, axis=0)
sd = numpy.std(elements, axis=0)
print("mean:", mean)
print("std:", sd)

final_list = [x for x in arr if (x > mean - 2 * sd)]
final_list = [x for x in final_list if (x < mean + 2 * sd)]
print(final_list)
