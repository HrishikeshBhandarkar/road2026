def length(list):#Functions and others
 print(len(list))

le=[3,5,7,5,4]
print(le)
length(le)

def prili(list):
 for i in range (len(list)): 
  print(list[i],end="	")
print("Printing list in a single line")
prili(le)
def fac(n):
 
 if n==0 or n==1:
   return 1
 else:
  return n*fac(n-1)
print('\n')
n=int(input("Enter a number to find the factorial = "))
print(fac(n))


def uti(usd):
 print("RUPEES",usd*94)

u=float(input("Enter USD = "))
uti(u)

def sum(n):
 if n ==0: return 0
 else: 
    return n+sum(n-1)

g=int(input("Enter a number = "))
print(sum(g))


