# Given the weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

# I/P:  arr = [(120, 30), (100, 20), (60, 10)]      W = 50
# O/P:  max_value = 240

def fractionalKnapsack(arr, W):
    n = len(arr)
    ratio = []

    for i in range(n):
        val = arr[i][0]
        wgt = arr[i][1]
        ratio.append((val, wgt, val / wgt))
    sorted_ratio = sorted(ratio, key=lambda x: x[2], reverse=True)
    final_value = 0

    for curr in sorted_ratio:
        if curr[1] <= W:
            final_value = final_value + curr[0]
            W = W - curr[1]
        else:
            final_value = final_value + curr[0] * (W / curr[1])
            break
    return final_value


arr = [(120, 30), (100, 20), (60, 10)]
W = 50
print(fractionalKnapsack(arr, W))
