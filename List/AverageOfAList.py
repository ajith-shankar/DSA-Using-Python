# Find average or mean of a list

# Solution 1:

def average(l):
    sum = 0
    for i in l:
        sum = sum + i
    n = len(l)
    return sum / n


def main():
    l = [10, 35, 47, 22, 8]
    print(f"Solution 1: The average of the list {l} is:", average(l))


if __name__ == "__main__":
    main()


# *********************************************************************************************

# Solution 2:

def mean(l):
    return sum(l) / len(l)


def main():
    l = [10, 35, 98, 47, 22, 11]
    # print(f"Solution 2: The average/mean of the list {l} is: ", round(mean(l), 2))
    print(f"Solution 2: The average/mean of the list {l} is:", mean(l))
    print(f"Solution 2: The average/mean of the list {l} is:", end=" ")
    print("%.2f" % mean(l))


if __name__ == "__main__":
    main()
