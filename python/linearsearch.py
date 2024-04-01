def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

my_list = [5,10,15,20,25,30,35,40,45,50]
target_element = 30
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")