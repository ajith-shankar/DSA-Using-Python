# Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1's in it.

# Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
# Output: 2

def count_ones(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2

        if 1 > arr[mid]:
            end = mid - 1

        elif 1 < arr[mid]:
            start = mid + 1

        else:
            if arr[mid] == 1 and arr[mid + 1] != 1:
                end = mid
    return 0


def main():
    arr = [1, 1, 0, 0, 0, 0, 0]
    print(f"Count of 1 is", count_ones(arr))


if __name__ == "__main__":
    main()
