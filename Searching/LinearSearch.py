# Linear search works for both sorted and unsorted array

# Input : [8, 9, 15, 7, 14, 23, 6, 30] search for 14
# Output : 4 (index)

# Time complexity: Best case: O(1) and Worst case: O(n)
# Space complexity: O(1)

def linear_search(arr, target):
    if len(arr) == 0:
        return -1

    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1


def main():
    arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
    target = 80
    res = linear_search(arr, target)
    if res != -1:
        print(f"Target element {target} is present at index:", res)
    else:
        print(f"Target element {target} is not present in the given array:", res)


if __name__ == "__main__":
    main()

