# Given a list of numbers, write a Python program to find the largest number in given list.

# Solution 1: Naive approach

def get_largest(lst):
    for x in lst:  # iterate over each element
        for y in lst:  # iterate over each element to compare
            if y > x:
                break
        else:
            return x
    return None


def main():
    lst = [10, 2, 3, 20, 5, 100]
    print(f"Solution 1: The largest element is:", get_largest(lst))


if __name__ == "__main__":
    main()


# Time complexity: O(n^2)

# ***********************************************************************************************

# Solution 2: Naive approach

def get_largest(lst):
    res = lst[0]
    for ele in lst:
        if ele > res:
            res = ele
    return res


def main():
    lst = [10, 2, 3, 20, 5, 258]
    print(f"Solution 2: The largest element is:", get_largest(lst))


if __name__ == "__main__":
    main()

# Time complexity: O(n)

# *********************************************************************************************

# Solution 3: Using built-in function

def get_largest(lst):
    return max(lst)


def main():
    lst = [10, 2, 582, 20, 5, 234]
    print(f"Solution 3: The largest element is:", get_largest(lst))


if __name__ == "__main__":
    main()
