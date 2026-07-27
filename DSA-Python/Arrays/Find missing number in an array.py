def miss_num(array):
    n=len(array)+1
    ex=(n * (n - 1)) // 2
    mn=ex - sum(array)
    return mn
u=[0,1,2,3,4,5,6,8]
print(u)
print(miss_num(u))