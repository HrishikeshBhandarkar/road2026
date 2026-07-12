# Printing factors of a given number
from math import sqrt
a = int(input("Enter a number = "))
fact=[]
for i in range(1,int(sqrt(a))+1):
    if a%i == 0:
        fact.append(i)
        if i != a/i:
            fact.append(a/i)
print(sort(fact))