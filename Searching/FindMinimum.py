# Find minimum element in an array

def find_mini(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < ans:
            ans = arr[i]

    return ans


if __name__ == "__main__":
    arr = [20, 2, 14, -7, -1, 25, 33]
    res = find_mini(arr)
    print(res)
