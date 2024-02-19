a=[2,3,5]
b=[2,4,6,8]
a.append(5) #insert value
a.extend(b) #merge two list
print(len(a)) #lenght of list
print(a.count(2)) #no of val
print(a.index(8)) #place of val
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)
a.pop(2)
print(a)
b = a.copy()
print(b)