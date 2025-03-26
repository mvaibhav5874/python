#this code is for count the arry and find element
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
