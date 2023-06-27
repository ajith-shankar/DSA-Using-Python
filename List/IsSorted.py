# Write a program to check whether the list is sorted or not

# Solution 1: Efficient approach

def is_sorted(lst):
    if len(lst) == 0 or len(lst) == 1:
        return True

    i = 1
    while i < len(lst):
        if lst[i] < lst[i - 1]:
            return False
        i = i + 1
    else:
        return True


def main():
    lst = [10, 3, 5, 20, 40, 50]
    if is_sorted(lst):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(1)

# *********************************************************************************************

# Solution 2: Using bulit-in function
# sorted() returns new list

def is_sorted(lst):
    lst2 = sorted(lst)

    if lst2 == lst:
        return True
    else:
        return False


def main():
    lst = [1, 3, 5, 20, 20, 40, 50]
    if is_sorted(lst):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()


# Time complexity: O(n)
# Space complexity: O(1)

# *****************************************************************************

def is_sorted(arr):
    n = len(arr)

    if n == 1:
        return 1

    asc_count = 0
    desc_count = 0

    # for ascending array
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            asc_count += 1

        if asc_count == n-1:
            return 1

    # for descending array
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            desc_count += 1

        if desc_count == n-1:
            return 1

    else:
        return 0


arr = [1, 1, 2, 2, 3]
print(is_sorted(arr))


