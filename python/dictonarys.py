from typing import Dict

Dict ={'vaibhav':'0097', 'dileep':'0009'}
print(Dict['vaibhav'])
print(Dict['dileep'])
for x in Dict:
    print(x)
    print(Dict[x])#first way
for x,y in Dict.items():
    print(x)
    print(y)#second way
Dict['vaibhav'] = '70097'
print(Dict['vaibhav'])
Dict['divyansh'] = '70104'
print(Dict['divyansh'])