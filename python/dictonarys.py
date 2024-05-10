from typing import Dict

names = [('vaibhav', 70097),('dileep', 70009)]
allnames = [('divyansh', 70104),('abhi', 0)]
print(names)
print(allnames)
my_names = {k: v for k, v in names}
print(type(my_names))
my_allnames = {k: v for k, v in allnames}
print(type(my_allnames))
my_names.update(allnames)
print(my_names)
print(my_names['vaibhav'])
print(my_names['divyansh'])
my_allnames.setdefault('abhi', 700109)
print(my_allnames['abhi'])
for x, y in my_names.items():
    print(x)
    print(y) #second way
print(my_names['vaibhav'])
print(my_allnames['divyansh'])
