# Write a python program to print Union of Two sorted arrays,
# where union is sorted and doesn't contain duplicate element

# Input: a = [3, 5, 8]      b = [2, 8, 9, 10, 15]
# Output: [2, 3, 5, 8, 9, 10, 15]

# Input: a = [2, 3, 3, 3]       b = [3, 4, 4]
# Output: [2, 3, 4]


# Solution 1: Naive approach

# def union_sol1(a, b):
#     c = a + b  # O(m+n) where m=len(a) and n=len(b)
#     c.sort()  # O((m+n) * log(m+n))
#     for i in range(0, len(c)):
#         if i == 0 or c[i] != c[i - 1]:
#             print(c[i], end=" ")  # O(m+n)
#
#
# a = [2, 3, 3, 3]
# b = [3, 4, 4]
# union_sol1(a, b)


# Time complexity: O((m+n) * log(m+n))

# -----------------------------------------------------------------------------------------

# Solution 2: Efficient approach (using Merge sort)

def union_sol2(arr1, arr2):
    i = j = 0

    # main loop for process two arrays
    while i < len(arr1) and j < len(arr2):

        # if previous element and current element is same (duplicates) of array1
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1

        # if previous element and current element is same (duplicates) of array2
        elif j > 0 and arr2[j] == arr2[j - 1]:
            j += 1

        # if array1 element is lesser than array2 element
        elif arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i += 1

        # if array2 element is lesser than array1 element
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1

        # if array1 and array2 elements are same, print that element only one time
        else:
            print(arr1[i], end=" ")
            i += 1
            j += 1

    # to process leftover element of the array1
    while i < len(arr1):
        if i > 0 and arr1[i] != arr1[i - 1]:
            print(arr1[i], end=" ")
        i += 1

    # to process leftover elements of the array2
    while j < len(arr2):
        if j > 0 and arr2[j] != arr2[j - 1]:
            print(arr2[j], end=" ")
        j += 1


def main():
    arr1 = [3, 5, 8]
    arr2 = [2, 8, 9, 10, 15]
    union_sol2(arr1, arr2)


if __name__ == "__main__":
    main()

# Time complexity: O(m+n)
# Space complexity: O(1)
