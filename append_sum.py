def append_sum(lst):
    i=0
    while i < 3:
        calc = lst[-2] + lst[-1]
        final = lst.append(calc)
        i+=1
    return lst




print(append_sum([1, 1, 2]))