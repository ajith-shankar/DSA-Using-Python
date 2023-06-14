# Given list and left rotate it by one

# lst=[10, 20, 30, 40] after left rotate by one lst=[20, 30, 40, 10]

# Solution 1: Using list slicing
def left_rotate(lst):
    lst = lst[1:] + lst[0:1]
    return lst


def main():
    lst = [10, 20, 30, 40]
    lr_lst = left_rotate(lst)
    print(f"Solution 1: After left rotate by one", lr_lst)


if __name__ == "__main__":
    main()


# ********************************************************************************************

# Solution 2: Using append & pop method

def left_rotate(lst):
    lst.append(lst.pop(0))
    return lst


def main():
    lst = [15, 22, 50, 30]
    lr_lst = left_rotate(lst)
    print(f"Solution 2: After left rotate by one", lr_lst)


if __name__ == "__main__":
    main()


# ******************************************************************************************

# Solution 3: Iterative method

def left_rotate(lst):
    size = len(lst)
    first_ele = lst[0]
    for i in range(1, size):
        lst[i-1] = lst[i]

    lst[size-1] = first_ele
    return lst


def main():
    lst = [200, 100, 540, 76, 896]
    lr_lst = left_rotate(lst)
    print(f"Solution 3: After left rotate by one", lr_lst)


if __name__ == "__main__":
    main()

