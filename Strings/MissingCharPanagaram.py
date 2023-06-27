# You are given a string s. You need to find the missing characters in the string to make a panagram
# Note: The output characters will be lowercase and lexicographically sorted.

# i/p : s = "Abcdef"                 o/p : "ghijklmnopqrstuvwxyz"
# i/p : s ="abcxyzdefghijpqrstklmnouvw"  o/p : -1

def missingPanagram(s):
    present = [False] * 26

    for i in range(len(s)):
        # traverse all char and if char present, mark present array index as True
        if 'a' <= s[i] <= 'z':  # s[i] >= 'a' and s[i] <= 'z'
            present[ord(s[i]) - ord('a')] = True
        elif 'A' <= s[i] <= 'Z':  # s[i] >= 'A' and s[i] <= 'Z'
            present[ord(s[i]) - ord('A')] = True

    res = ""

    for i in range(len(present)):
        if not present[i]:  # present[i] == False
            res = res + chr(i + ord('a'))

    if res != "":
        return res
    else:
        return -1


#s = "abcxyzdefghijpqrstklmnouvw"
#s = "RpUjchlgQnpMmILQCuRrPkZpHhgoBEmsfYkzMtlXHhKEqXgMSuJUQBsxLBVAYwLFAWyIekUMhbCWWMDXveohzpp"
s = "Abcdef"
print(missingPanagram(s))

