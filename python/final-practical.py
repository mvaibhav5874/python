t = 2, 4, 6, 8
print(t)
print(type(t))

a = (1,)
print(a)
print(type(a))

li1 = [1, 3, 5, 7, 9]
z = tuple(li1)
print(z)
print(type(z))

merge= a+t
print(merge)
print(type(merge))

repeated_tuple = (19, 29, 39) * 2
print("Repeated tuple:", repeated_tuple)

d = ((1, 3, 5), (2, 4, 6))
print("Nested Tuple:", d)

print(len(t))

print("count of tuple", merge.count(2))

tuple2 = merge[1:6]
print(tuple2)

del (tuple2)