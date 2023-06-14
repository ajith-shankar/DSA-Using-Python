# Write a python program to print Intersection of two sorted arrays,
# where Intersection is sorted and doesn't contain duplicate element

# Input: a = [1, 20, 20, 40, 60]      b = [2, 20, 20, 20]
# Output: [2, 20]

# Solution 1: Naive approach
# it is not handling duplicate elements

# def intersection_sol1(a, b):
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             i += 1
#         elif b[j] < a[i]:
#             j += 1
#         else:
#             print(a[i], end=" ")
#             i += 1
#             j += 1
#
#
# a = [1, 20, 20, 40, 60]
# b = [2, 20, 20, 20]
# intersection_sol1(a, b)
#

# -----------------------------------------------------------------------------------------

# Solution 2: Efficient approach (using Merge sort)

def intersection_sol2(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if i > 0 and a[i] == a[i-1]:
            i += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            print(a[i], end=" ")
            i += 1
            j += 1


a = [1, 20, 20, 40, 60]
b = [2, 20, 20, 20]
intersection_sol2(a, b)

# Time complexity: O(m+n) where m=len(a) and n=len(b)
# Space complexity: O(1)
