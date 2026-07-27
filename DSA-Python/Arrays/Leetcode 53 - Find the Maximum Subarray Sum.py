def maxi(array):
    n=len(array)
    i=0
    total=0
    maximum=float("-inf")
    while i<n:
        if total<0:
            total=0
        total+=array[i]
        maximum=max(maximum,total)
        i+=1
    return maximum
o=[-2,1,-3,4,-1,2,1,-5,4]
print(o)
ma=maxi(o)
print(ma)

        