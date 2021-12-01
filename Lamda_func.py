# my_lambda = lambda x: x**3
# print(my_lambda(7))

# my_letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list(map(str.capitalize, my_letters)))
# # print([str.capitalize for letter in my_letters])
# print(list(map(lambda x:x+x.capitalize(), my_letters)))

from random import randint
my_ints = [randint(1,1000) for num in range(100)]
print(my_ints)