# Square brackets can be used to access elements of the string.

print(ord("a"))  # ord() gives you ascii value of the character
print(ord("A"))

print(chr(97))  # chr() gives you english character of the ascii value
print(chr(65))

s = "Geek"
print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])

# strings are immutable, you can't modify it

s = "Geek"
# s[0] = "g"  # throws TyperError
print(s)

s = """Hi,
This is "Python" course
Hello World"""
print(s)

s1 = "C:\DSA\name.py"  # \n will create the new line
print(s1)

# raw string
s2 = r"C:\DSA\name.py"  # here r will prevent escape feature
print(s2)

s3 = "\\t"  # to print \t
print(s3)

name="ABC"
Course = "Python"

# f string
s = f"Hi {name}, Welcome to the {Course} course"
print(s)

a = 10
b = 20
print(f"addition of {a} and {b} is {a+b}")

s1 = "abc"
print(f"Upper case of {s1} is {s1.upper()}")

