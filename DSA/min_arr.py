"""A sorted array arr[] (may contain duplicates) is rotated at some unknown point, the task is to find the minimum element in it.
Examples:
Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array."""

class Solution:
    def findMin(self, arr):
        # complete the function here
        min_val = arr[0]
        for i in range(1, len(arr)):
            if arr[i]< min_val:
                min_val = arr[i]
            return min_val

arr = [5, 6, 1, 2, 3, 4]
print(Solution().findMin(arr))