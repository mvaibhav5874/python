"""Find All Triplets with Zero Sum
Difficulty: Medium
Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero.
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0"""
class Solution:
    def findTriplets(self, arr):
        # Your code here
        res = []
        index = dict()
        for i in range(len(arr)):
            if arr[i] in index:
                index[arr[i]].append(i)
            else:
                index[arr[i]] = [i]
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                sumi = arr[i] + arr[j]
                if -sumi in index:
                    for curr_index in index[-sumi][::-1]:
                        if curr_index <= j:
                            break
                        res.append([i, j, curr_index])

        res.sort()
        return res