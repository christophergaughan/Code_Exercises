string = "Reverse This!"

def rev_string(string):
    rev = ''
    for letter in string:
        rev = letter + rev
    return rev

print(rev_string(string))