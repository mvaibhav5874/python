"""n = int(input("Enter the value of n"))
i = 1
prod = 1
while(i<=n):
    prod = prod*i
    i+=1
print(prod)"""
n = int(input("Enter the value of n"))
i = 1
while(i<=n):
    j=1
    while(j<=i):
        print("*", end = " ")
        j+=1
    print(" ")
    i+=1