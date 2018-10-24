import numpy

arr = [-1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]

elements = numpy.array(arr)


def outliers_iqr(ys):
    quartile_1, quartile_3 = numpy.percentile(ys, [10, 90])
    print("q1:", quartile_1)
    print("q3:", quartile_3)
    iqr = quartile_3 - quartile_1
    print("iqr", iqr)
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    print("lower_bound", lower_bound)
    print("upper_bound", upper_bound)
    final_list = [x for x in arr if (x > lower_bound)]
    final_list = [x for x in final_list if (x < upper_bound)]
    return final_list


res = outliers_iqr(arr)
print(res)
