#


def countWords(s):
    n = len(s)
    count = 0

    if not s:
        return -1

    for i in range(n):
        if s[i] == " ":
            count += 1

    return count+1


#s = ""
s = "Welcome to Python"
print(countWords(s))
