def re_arra(array):
    n=len(array)
    result=[0]*n
    p,ne=0,1
    for i in array:
        if i>0:
            result[p]=i
            p+=2
        if i<0:
            result[ne]=i
            ne+=2
    return result
o=[5,10,-3,-1,-10,6]
print(o)
print(re_arra(o))
 