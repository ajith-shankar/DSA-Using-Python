# The Pattern Searching algorithms are sometimes also referred to as String Searching Algorithms and are considered as a part of the String algorithms. These algorithms are useful in the case of searching a string within another string.

# i/p : txt="Geeks for Geeks"       pat="eks"           o/p : 2, 12 (indexes)
# i/p : txt="AAAAA"                 pat="AAA"           o/p : 0, 1, 2


# 1. Using find() method

def patternSearching1(txt, pat):
    pos = txt.find(pat)
    while pos >= 0:
        print(pos)
        # for next occurrence
        pos = txt.find(pat, pos+1)


txt = "Geeks for Geeks"
pat = "eks"
patternSearching1(txt, pat)


# **************************************************************

# 2. Naive approach

def patternMatching2(txt2, pat2):
    t = len(txt2)
    p = len(pat2)

    for i in range(t - p + 1):
        j = 0
        while j < p:
            if pat[j] != txt[i+j]:
                break
            j = j + 1

        if j == p:
            print(i, end=" ")


txt = "Geeks for Geeks"
pat = "eks"
patternMatching2(txt, pat)


# Time complexity: O((t-p+1)*p)
# Space complexity: O(1)

# **********************************************************************************


# 3. Naive solution for Distinct char in the pattern

def patternSearching3(txt3, pat3):
    t = len(txt3)
    p = len(pat3)
    i = 0
    while i <= (t-p):
        for j in range(p):
            if pat[j] != txt[i+j]:
                break
        if j == p:
            print(i, end=" ")

        if j == 0:
            i += 1
        else:
            i += j


txt = "ABCEABFABCD"
pat = "ABCD"
patternSearching3(txt, pat)



