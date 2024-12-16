my_arr = [1,36,7,26,78]
target=7


def linear_search(arr,target):
    n = len(arr)
    for i in range(1,n):
        if arr[i]==target:
            return i
        else:
            i+=1

print('target found at :',linear_search(my_arr,target))