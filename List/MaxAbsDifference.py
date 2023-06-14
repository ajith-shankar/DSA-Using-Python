# Given an array arr[] of N integers, the task is to find the maximum absolute difference
# between any two elements of the array.

# Input: arr[] = {2, 1, 5, 3}
# Output: 4
# |5 – 1| = 4

# Input: arr[] = {-10, 4, -9, -5}
# Output: 14
# |-9 - -5| = |-14| = 14

# Solution 1: Naive approach

def max_abs_diff(lst, n):
    res = lst[1] - lst[0]
    for i in range(0, n-1):
        for j in range(i+1, n):
            res = max(res, abs(lst[j] - lst[i]))

    return res


def main():
    lst = [2, 3, 10, 6, 4, 8, 1]
    n = len(lst)
    print(f"Solution 1: The maximum absolute difference is:", max_abs_diff(lst, n))


if __name__ == "__main__":
    main()


# Time complexity: O(n^2)
# Space complexity: O(1)

# ********************************************************************************************

# Solution 2: Efficient approach

def max_abs_diff(lst, n):
    min_ele = lst[0]
    max_ele = lst[0]
    for i in range(0, n):
        min_ele = min(min_ele, lst[i])
        max_ele = max(max_ele, lst[i])

    return max_ele - min_ele


def main():
    lst = [2, 3, 10, 6, 4, 8, 1]
    n = len(lst)
    print(f"Solution 2: The maximum absolute difference is:", max_abs_diff(lst, n))


if __name__ == "__main__":
    main()

# Time complexity: O(n)
# Space complexity: O(1)
