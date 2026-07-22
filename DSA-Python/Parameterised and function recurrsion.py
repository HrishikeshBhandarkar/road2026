#Sum of n natural numbers
def s(n):
    if n==0:
        return 0
    else: return n+s(n-1)
print(s(10))



#To find factorial of a number using recurssion
def fac(num):
    if num==0 or num==1:
        return 1
    else :
        return num*(fac(num-1))
print(fac(5))