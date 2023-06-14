# https://leetcode.com/problems/find-in-mountain-array/

# Given a mountain array return the minimum index of the target element

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

# Approach:
# 1. Find the peak element
# 2. Search in the first half (ascending order)
# 3. If not found search in second half (descending order)


# Answer
# ----------
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.peak_element(mountain_arr)
        idx_1 = self.search_asc_desc(mountain_arr, target, 0, peak, isAsc=True)
        idx_2 = self.search_asc_desc(mountain_arr, target, peak, mountain_arr.length() - 1, isAsc=False)
        if idx_1 == -1:
            return idx_2
        if idx_2 == -1:
            return idx_1
        if idx_1 > idx_2:
            return idx_2
        else:
            return idx_1

    def peak_element(self, mountain_arr):
        start = 0
        end = mountain_arr.length() - 1

        while start < end:
            mid = start + (end - start) // 2

            # decreasing part of the array
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                end = mid

            else:  # arr[mid] < arr[mid + 1]
                start = mid + 1
        return start

    def search_asc_desc(self, mountain_arr, target, start, end, isAsc=True):
        while start <= end:
            # find middle element
            mid = start + (end - start) // 2

            # if target is present at the middle
            if target == mountain_arr.get(mid):
                return mid

            # for ascending order
            if isAsc:
                # if target element is lesser than mid
                if target < mountain_arr.get(mid):
                    end = mid - 1

                # if target element is greater than mid
                else:
                    start = mid + 1

            # for descending order
            else:
                # if target element is greater than mid
                if target > mountain_arr.get(mid):
                    end = mid - 1

                # if target element is lesser than mid
                else:
                    start = mid + 1

        # if target element is not present in the array
        return -1
