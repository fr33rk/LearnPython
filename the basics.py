# Indentation and block structuring

# Comments
# assign 5 to x
x = 5
x = 3 # now it is 3
x = "# This is not a comment"

print(x)

# Use del to remove a variable
del x

# Optional hints
def add_ints(x, y):
    return x + y

def add_ints_hints(x: int, y: int) -> int:
    return x + y

print(add_ints(21, 21.9))

print(add_ints_hints(21, 21.9))

# strings
x = "Hello world"
x = "\t this string starts with a \"tab\"."
print(x)
print("this string contains a single backslash \\")
print("Double quotes")
print('Single quote')
print("""
Multiline
using three double quotes
""")

# numbers
# Div to float
x = 10 / 3
print(x)
# Div to int
x = 10 // 3
print(x)

# Type casting
f = 21.09
i = int(f)
print(i)
i = 2e2
print(i)

#Build int numeric functions
print(abs(-2109))
print(divmod(100, 11))
print(float(2109))
print(hex(2109))
print(oct(2109))
print(pow(2, 2))
print(round(2109.2109, 2))

#Rest in math
from math import sin, cos, tan
print(sin(90))
print(cos(45))
print(tan(180))

this_is_not_initialize = None
print(this_is_not_initialize)

#input from user
magic_number = input("Magic number:")
magic_number = float(magic_number) * 21.09 - sin(1978)
print(magic_number)

