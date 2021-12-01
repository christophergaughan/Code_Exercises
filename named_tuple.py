from collections import namedtuple
# with named tuple you can pass in a list or comma dilineated strings
User = namedtuple('User', 'user, username, email, pw')
print(type(User))
christopher = User('Chris', 'Crane', 'crane@gmail', '1234')
print(christopher)
User2 = namedtuple('User', ['user', 'username', 'email', 'pw'])
dane = User2('Daniel', 'Dane', 'dane@gmail', 'abcdef')
print(dane)
print(christopher[0:3])
print(dane[1:3])
print(christopher.user)
# you can print as an ordered dictionary 
print(christopher._asdict())
# you can only do this as a named tuple and not with an ordinary tuple
print(dane._replace(pw='4567'))
# Remember, this does not happen 'inplace', you will have to end up reassigning the variable
dane = dane._replace(pw='4567')
print(dane)