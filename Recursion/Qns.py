import re
txt = "Abc"
print(re.search("[Aa]bc", txt))

tech = "Python"
print(tech*len(tech))

x=[10, 20]
z=x[:]
y=x
y[1]=30
print(x[1])

a="    PYTHON PROGRAMMER      "
print(a.lstrip('p'))

a = "Malaavikaa"
print(re.sub('a,(2)', '*', a,))

sum = 0
pattern = "py"
if re.match(pattern, 'python.txt'):
    sum += 1
if re.match(pattern, 'text.py'):
    sum +=2
if re.search(pattern, 'herepyfile'):
    sum +=4
if re.search(pattern, 'numpy'):
    sum += 8
print(sum)