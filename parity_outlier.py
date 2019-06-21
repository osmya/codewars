def find_outlier(integers):
    outlier_odd = [i for i in integers if i % 2 != 0]
    outlier_even = [i for i in integers if i % 2 == 0]
    if len(outlier_odd) > len(outlier_even):
        return outlier_even[0]
    else:
        return outlier_odd[0]
