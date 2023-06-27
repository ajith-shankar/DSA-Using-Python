# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

def immediate_smaller(arr, x):
    n = len(arr)
    smaller = -1
    for i in range(n):
        if smaller < arr[i] < x:  # arr[i] > smaller and arr[i] < x
            smaller = arr[i]

    return smaller


arr = [4, 67, 13, 12, 15]
x = 16
print(immediate_smaller(arr, x))


