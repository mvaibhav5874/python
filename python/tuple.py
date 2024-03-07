t = 2, 4, 6, 8, 10
print(t)
print(type(t))  # creation of normal tuple

a = (1,)

print(a)
print(type(a))  # creation of single tuple

list1 = [1, 3, 5, 7, 9]
z = tuple(list1)
print(type(z))  # creation of tuple using constructor

rest = t + a
print("concatenation", tuple(rest))  # concatenation of two tuples

repeated_tuple = (19, 29, 39) * 2
print("Repeated tuple:", repeated_tuple)  # creation of nested tuple

d = ((1, 3, 5), (2, 4, 6))
print("Nested Tuple:", d)  # creation of nested tuple

print(len(t))  # printing the length of tuple

print("count of tuple", rest.count(2))  # count cretain no count

tuple2 = rest[1:6]
print(tuple2)  # printing the tuple using index

del t

string_tuple = "vaibhav", "surya"
contadinate_both = string_tuple[0][0] + string_tuple[1][0]
print(contadinate_both)

string_tuple = "vaibhav"
contadinate_both = string_tuple[0] + string_tuple[1]
print(contadinate_both)
