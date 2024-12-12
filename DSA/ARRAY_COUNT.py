"""QUESTION :-Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[].
Examples :
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4."""
class Solution:
    def countFreq(self, arr, target):
        count = 0
        for i in range(len(arr)):
            if(arr[i] == target):
                count += 1
        return count

arr = [1,2,3,4,5,6,7,20]
target = 2

print(Solution().countFreq(arr, target))