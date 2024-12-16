"""Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray.

Examples:

Input: arr[] = [1,2,3,7,5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12."""

class Solution:
    def subArraySum(self, arr, target):
        i = j = 0
        while (j != len(arr)):

            if target == arr[j]:

                return [i + 1, j + 1]

            elif target > arr[j]:

                target -= arr[j]

                j += 1

            else:

                target += arr[i]

                i += 1

        return [-1]