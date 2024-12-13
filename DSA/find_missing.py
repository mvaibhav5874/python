"""You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive).
This array represents a permutation of the integers from 1 to n with one element missing.
Your task is to identify and return the missing element.
Examples:
Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4."""

class Solution:
    def missingNumber(self, arr):
        x = set(arr)
        for i in range(len(arr)+1):
            if i+1 not in x:
                return i+1

arr= [1,2,3,4,5,6,8,9]
print(Solution().missingNumber(arr))