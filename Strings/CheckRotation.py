# Given two string we need to check whether they are rotation of each other or not
# S2 can be obtained by S1 by rotating(clock wise or anti clock wise) S1 any no of time

# i/p : S1="ABCD"  S2="CDAB"
# O/P : Yes     (ABCD-->BCDA--->CDAB)

def checkRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = ""
    temp = s1 + s1  # ABCD + ABCD = ABCDABCD
    return temp.find(s2) != -1


if __name__ == "__main__":
    str1 = "ABCD"
    str2 = "CDAB"
    print(checkRotation(str1, str2))

# Time complexity: O(N)
# Space complexity: O(1)
