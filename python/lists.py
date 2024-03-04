list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []

for x in list1:
    list2.append(x + 10)
    print(list2)

list2 = [x + 10 for x in list1]
print(list2)

#tuple_list1 = tuple(list1)
#print(type(tuple_list1))
