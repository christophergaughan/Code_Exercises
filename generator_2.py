l1 = [num for num in range(1,11)]

# my_cubed_ints = map(lambda x: x**3, l1)
# print(list(my_cubed_ints))
def mash_map(f, iterable):
    for item in iterable:
        yield f(item)
        
# for regular function with list comprehension       
# def mash_map(f, iterable):
#     return [f(item) for item in iterable]

# for generator 
def mash_map(f, iterable):
    yield (f(item) for item in iterable)
    
# You will only get the generator object if you do the above. THUS:
print(l1)
my_cubed_ints = mash_map(lambda x: x**3, l1)
print(list(my_cubed_ints))

    
    
        
# print(l1)
# my_cubed_ints = mash_map(lambda x: x**3, l1)
# print(my_cubed_ints)
# print(next(my_cubed_ints))
# print(next(my_cubed_ints))
# print(next(my_cubed_ints))
# print(list(my_cubed_ints))