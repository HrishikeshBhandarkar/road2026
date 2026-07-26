def move_zero(list1):
    n=len(list1)
    if n==1:
        return
    i=0
    while i<n:
        if list1[i]==0:
            break
        i+=1
    if i==n:
        return
    j=i+1
    while j<n:
        if list1[j]!=0:
            list1[i],list1[j]=list1[j],list1[i]
            i+=1
        j+=1
v=[2,1]
print(v)
move_zero(v)
print(v)