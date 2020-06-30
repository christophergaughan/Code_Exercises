#!/usr/bin/python
"""
Create a function named always_false() that has one parameter named num.

Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.
"""
def always_false(num):
	if 10 > num < 20:
		return False
	else:
		return False
		
	