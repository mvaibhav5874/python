my_arr = [2,43,576,27,89,49]

n = len(my_arr)
for i in range(n):
    for j in range(i+1,n):
        if my_arr[i]>my_arr[i+1]:
            my_arr[i],my_arr[i+1]=my_arr[i+1],my_arr[i]

print('sorted array',my_arr)