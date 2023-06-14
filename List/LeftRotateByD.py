# Given list and left rotate it by D places

# lst=[10, 20, 30, 40, 50, 60] after left rotate by D=3 places lst=[40, 50, 60, 10, 20, 30]

# Solution 1: List slicing

def left_rotate(lst, d):
    return lst[d:] + lst[:d]


def main():
    lst = [10, 20, 30, 40, 50, 60, 70]
    d = 3
    print(f"Solution 1: Left rotate by {d} places", left_rotate(lst, d))


if __name__ == "__main__":
    main()


# *********************************************************************************************

# Using pop() and append()

def left_rotate(lst, d):
    for i in range(0, d):
        lst.append(lst.pop(0))

    return lst


def main():
    lst = [20, 40, 60, 80, 100, 30, 50]
    d = 2
    print(f"Solution 2: Left rotate by {d} places", left_rotate(lst, d))


if __name__ == "__main__":
    main()


# Time Complexity: O(nd)
# Space Complexity:
# ***************************************************************************************************

# Solution 3: Most efficient approach

def left_rotate(lst, d):
    n = len(lst)
    reverse(lst, 0, d - 1)
    reverse(lst, d, n-1)
    reverse(lst, 0, n-1)

    return lst


def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


def main():
    lst = [10, 20, 30, 40, 50]
    d = 2
    print(f"Solution 3: Left rotate by {d} places", left_rotate(lst, d))


if __name__ == "__main__":
    main()


# Time Complexity: O(nd)
# Space Complexity: O(1)

# ***********************************************************************************************
