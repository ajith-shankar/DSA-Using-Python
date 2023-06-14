# Write a program to separate the given list into Even and Odd list

# Solution 1

def even_or_odd(ls):
    even = []
    odd = []
    for i in ls:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd  # return tuples


def main():
    ls = [10, 13, 20, 25, 32, 40]
    even, odd = even_or_odd(ls)  # unpacking of tuples, now it will become list
    print("Even list:", even)
    print("Odd list:", odd)
    # print(even_or_odd(ls)) # it prints tuple ([10, 20, 32, 40], [13, 25])


if __name__ == "__main__":
    main()
