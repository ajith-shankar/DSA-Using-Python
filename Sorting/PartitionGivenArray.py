# Foundation for Quick sort

# write a program to partition an array in such a way
# left the partition pointer contains elements which are lesser than the partition pointer element
# and right side it contains elements which are greater than the partition pointer element

# Input: a = [3, 8, 12, 6, 10, 7]    P = 5 (index)
# Output: a = [3, 6, 7, 8, 10, 12] or [6, 3, 7, 12, 8, 10]

# Explanation: here PP = 5 therefore PP ele = 7. left of PP ele contains element ele <= PP ele
# right side ele > PP ele. Left and right side, order of elements doesn't matter.
# Expected time complexity is O(N)


# Solution 1: Naive approach

def parti(arr, p):
    n = len(arr)
    temp = []
    # swap pp ele to the end
    arr[p], arr[n - 1] = arr[n - 1], arr[p]

    # move elements which are lesser than and equal to PP ele into new list
    for ele in arr:
        if ele <= arr[n - 1]:
            temp.append(ele)

    # now move the elements which are greater than PP ele at the end new list
    for ele in arr:
        if ele > arr[n - 1]:
            temp.append(ele)

    # now copy the temp elements to original list
    for i in range(len(arr)):
        arr[i] = temp[i]

    print(arr)


arr = [3, 8, 12, 6, 10, 7]
p = 5
parti(arr, p)

# Time complexity: O(N)
# Space complexity: O(N)
# Traversal: 3


# --------------------------------------------------------------------------------------------


# Solution 2: Lomuto partition
# here last element is considered as the pivot element

def lomuto(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        # current ele is lesser than pivot element
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place the pivot ele at its correct position
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def main():
    arr = [3, 8, 12, 6, 10, 7]
    l = 0
    h = 5
    print(lomuto(arr, l, h))
    print(arr)


if __name__ == "__main__":
    main()


# Time complexity: O(N)
# Space complexity: O(1)
# Traversal: 1

# ------------------------------------------------------------------------------------------


# Solution 3: Hoare's Partition
# here first element is considered as the pivot element

#def hoare(arr, l, h):
