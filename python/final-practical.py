t = 2, 4, 6, 8
print(t)
print(type(t))

a = (1,)
print(a)
print(type(a))

merge= a+t
print(merge)
print(type(merge))

li1 = [1, 3, 5, 7, 9]
z = tuple(li1)
print(z)
print(type(z))

repeated_tuple = (19, 29, 39) * 2
print("Repeated tuple:", repeated_tuple)

d = ((1, 3, 5), (2, 4, 6))
print("Nested Tuple:", d)

tuple2 = merge[1:6]
print(tuple2)

print("count of tuple", merge.count(2))

print(len(t))

del (tuple2)