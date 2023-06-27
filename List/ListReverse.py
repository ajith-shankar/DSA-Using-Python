def reverse_list(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


arr = [10, 20, 30, 40]
print(reverse_list(arr))

# Time complexity: O(N)
# Space complexity: O(1)

