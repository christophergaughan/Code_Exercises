
import string

## Methods and functions we can use on String objects
# Official documentation: https://docs.python.org/3/library
# We ran the following functions on strings
# len(), type(), id(), dir()
# We ran the following string methods
# capitalize(), upper(), lower(), strip(), find()
# split(), join()
# Test them out on the variable declaration below, two examples
# provided
greeting = "hello"
message = "i am christopher gaughan and I will be the instructor for this class. you will find me vulgar"
my_languages = ["Python", "Unix", "BASH", "HTML"]
my_list = [15, 24,  3, 45, 55, 6 , 7, 22]

print(len(greeting))
print(greeting.capitalize())
print(greeting.upper())
print(message.capitalize())
print(message.split())
print(" ".join(my_languages))
print('The minimum and maximum values in my_list are, respectively,', min(my_list), max(my_list))


# because I imported string
var = string.ascii_lowercase
print(var)

# We then looked at two ways of importing
# first the whole module like below
# import string

# Then we just imported what we need from the module like below
# from string import ascii_lowercase

# I have some variables defined below, go ahead and try
# the various functions and methods on them, I've started
# below by using the len function on the welcome_message
# variable
greeting = "hello"
user = "jon snow"
welcome_message = "hello jon snow, and welcome to the Algorithms course"
print(len(welcome_message))
print(greeting.upper())
print(greeting.lower())
print(welcome_message.split())
welcome_split = welcome_message.split()
print(len(welcome_split))

