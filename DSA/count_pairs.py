from collections import defaultdict
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        count=0
        di=defaultdict(list)
        for i,val in enumerate(arr):
            sume=target-val
            if sume in di:
                count+=len(di[sume])
            di[val].append(i)
        return count