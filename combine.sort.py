def combine_sort(lst1, lst2):
    lstall = lst1 + lst2
    lstall = sorted (lstall)
    return lstall



print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
