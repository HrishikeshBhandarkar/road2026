# Loops in Python

# 1. Print numbers from 1 to 100
print("Print numbers from 1 to 100")
for i in range (1,100):
 print(i)

for i in range (100,0,-1):
 print(i)

# Printing multiples of given number upto 10

s=int(input("Enter a num,ber = "))
for i in range (11):
 print(s*i)

# Printing elements of lists using loops

l=[1,4,9,16,25,36,49,64,81,100]
for i in range(10):
 print(l[i])

# searchimng in tuple using loop

l=(1,4,9,16,25,36,49,64,81,100)
print(l)
key=int(input("Enter a number = "))
i=0
while i<len(l):
 if(l[i]==key):
  print("Found at",i)
 else:
  print("finding")
 i+=1
 
# Sum of n numbers
n=int(input("Enter a number = "))
i=0
k=0
while i<=n:
 k+=i
 i+=1
print(k)


# factorial
print("factorial")
n=int(input("Enter a number = "))
z=1
for i in range(1,n+1): 
	z*=i
print(z)
