# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. Maximize the total profit if only one job can be scheduled at a time.

# Input:  Five Jobs with following deadlines and profits
# t = No of jobs to schedule

# JobID   Deadline  Profit
#   a            2          100
#   b            1          19
#   c            2          27
#  d            1          25
#  e            3          15

# Output: Following is maximum profit sequence of jobs: c, a, e


def jobSequence(arr, t):
    n = len(arr)

    # now sort the jobs according to their profit in decreasing order
    arr.sort(key=lambda x: x[1], reverse=True)

    # to keep track of free slots
    result = [False] * t

    # to store final sequence of job
    final_result = [-1] * t

    # iterate through all given jobs
    for i in range(n):
        # find the free slot for that job (find last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):  # min(t-1, deadline-1) & range(reverseOrder)
            # if free slot found
            if result[j] == False:
                result[j] = True
                final_result[j] = arr[i][0]
                break

    return final_result


if __name__ == "__main__":
    arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]
    t = 3
    print(jobSequence(arr, t))


# Time complexity: O(N^2)
# Space complexity: O(N)
