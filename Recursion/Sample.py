def abbreviation(ip_str):
    ip_str = ip_str.split(" ")
    res = []

    for ele in ip_str:
        if len(ele) == 2:
            res.append(ele[0].lower())
        if len(ele) > 2:
            res.append(ele[0].upper())
        if len(ele) < 2:
            continue

    return "".join(res)


def main():
    ip_str = "She has a coat"
    print("Solution 1: Output is:", abbreviation(ip_str))


if __name__ == "__main__":
    main()

# Time complexity: O(1)
# Space complexity: O(n)




