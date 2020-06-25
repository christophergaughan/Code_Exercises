"""
Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""


def large_power(base, exponent):
    assert isinstance (exponent, object)
    calc = base ** exponent
    if calc > 5000:
        return True, calc
    else:
        return False

print(large_power(6,7))
