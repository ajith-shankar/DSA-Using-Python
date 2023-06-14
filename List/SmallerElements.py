# Write a program to find the smaller elements to the target element in the list


# Solution 1:

def get_Smaller(lst, tar):
    res = []
    for ele in lst:
        if ele < tar:
            res.append(ele)
    return res


def main():
    lst = [10, 22, 35, 8, 76, 29, 3, 50, 11]
    tar = 20
    print(f"Solution 1: The smaller elements are:", get_Smaller(lst, tar))


if __name__ == "__main__":
    main()
