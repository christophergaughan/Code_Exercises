numbers = [1, 4, -3, 0, 7, -5, -0.03, 4]

# def extract_positive (numbers):
#     pos = []
#     for number in numbers:
#         if number > 0:
#             pos.append(number)
#     return pos

# print(extract_positive(numbers))   


# much faster filter() function 

# positive_numbers = filter(lambda n: n > 0, numbers)
# print(positive_numbers)    

# objects = [0, 1, [], 4, 5, "", None, 8]
# outpt = list(filter(None, objects)) 
# print(outpt)


numbers = [1, 3, 10, 45, 6, 50]
is_even = [number %2 ==0 for number in numbers]
# list(filter(is_even, numbers))
print(filter(is_even, numbers))
