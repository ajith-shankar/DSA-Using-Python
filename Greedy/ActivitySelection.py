# You are given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

# start[]  =  {10, 12, 20};
# finish[] =  {20, 25, 30};
# res = {0, 2}

# start[]  =  {1, 3, 0, 5, 8, 5};
# finish[] =  {2, 4, 6, 7, 9, 9};
# res = {0, 1, 3, 4}

# arr = [(12, 25), (10, 20), (20, 30)]
# res = 2

def maxActivities(arr):
    n = len(arr)
    # sort second part in ascending order
    arr.sort(key=lambda x: x[1])

    prev = 0
    res = 1  # we are considering 1st activity as final res

    for curr in range(1, n):  # bcz index[0] already considered for res
        if arr[curr][0] >= arr[prev][1]:
            res = res + 1
            prev = curr

    return res


if __name__ == "__main__":
    arr = [(12, 25), (10, 20), (20, 30)]
    print(maxActivities(arr))
