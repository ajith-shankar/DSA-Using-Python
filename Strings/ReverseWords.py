# Reverse words in a string   Space complexity should be O(1)

# i/p : s="I love programming"      o/p : "programming love I"
# i/p : s="abc"                     o/p : "abc"


# 1. Efficient approach

def reverse_helper(s1, b, e):
    while b < e:
        s1[b], s1[e] = s1[e], s1[b]
        b = b + 1
        e = e - 1
    return s1


def reverse_words(s):
    s2 = list(s)
    n = len(s2)
    begin = 0
    for end in range(n):
        if s[end] == " ":  # if we found space then reverse the word
            reverse_helper(s2, begin, end - 1)
            begin = end + 1  # now continue further

    reverse_helper(s2, begin, end)  # to reverse the last word (bcz there is no space after the last word, so in above for loop it doesn't get reversed we have to do it explicitly)

    reverse_helper(s2, 0, n-1)  # revere the whole string
    s2 = "".join(s2)  # ['D', 'S', 'A', ' ', 't', 'o', ' ', 'W', 'e', 'l', 'c', 'o', 'm', 'e'] ---> DSA to Welcome
    return s2


s = "Welcome to DSA"
print(reverse_words(s))


# Time complexity: O(N)

