array = [5,45,9,82,4,22]
size = len(array)
def selection_sort(array,size):
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if array[j]<array[min_index]:
                min_index= j
                array[i],array[min_index]=array[min_index],array[i]

selection_sort(array,size)
print("the sorted array using selection sort is:",array)