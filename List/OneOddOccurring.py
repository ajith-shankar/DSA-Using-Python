# Given an array of positive integers. All numbers occur an even number of times except one number
# which occurs an odd number of times

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3
#
# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5

# Solution 1: Using two loops

def odd_one_out(lst):
    size = len(lst)
    for i in range(0, size):
        count = 0
        for j in range(0, size):
            if lst[i] == lst[j]:
                count = count + 1
        if count % 2 != 0:
            return lst[i]
    return -1


def main():
    lst = [5, 7, 2, 7, 5, 2, 5]
    print(f"Solution 1: The odd number is:", odd_one_out(lst))


if __name__ == "__main__":
    main()


# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

# ********************************************************************************************

# Solution 2: Using bitwise XOR operator

# Here ^ is the XOR operators;
# Note:
# x^0 = x
# x^y=y^x (Commutative property holds)
# (x^y)^z = x^(y^z) (Distributive property holds)
# x^x=0

def odd_one(lst):
    res = 0
    for ele in lst:
        # XOR
        res = res ^ ele

    return res


def main():
    lst = [1, 2, 3, 2, 3, 1, 3]
    print(f"Solution 2: The odd number is:", odd_one(lst))


if __name__ == "__main__":
    main()

# Time Complexity: O(n)
# Auxiliary Space: O(1)
