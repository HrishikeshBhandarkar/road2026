def check_sorted(array):
    for i in range(len(array)-1):
        o=array[i]
        p=array[i+1]
        if o>p:
            return False
    return True
o=[1,2,3,4,5]
l=[3,32,134,4,3]
print(o)
print(check_sorted(o))
print(l)
print(check_sorted(l))
