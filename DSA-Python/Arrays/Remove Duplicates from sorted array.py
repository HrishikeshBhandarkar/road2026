def rem_dup(array):
    dic={}
    for i in array:
        dic[i]=dic.get(i,0)+1
    k=0
    for i in dic:
        array[k]=i
        k+=1
j=[1,1,2,3,4,4,5]
print(j)
rem_dup(j)
print(j)



#A better solution while taking two pointers


def r_d(array):
    if len(array)==1:
        return 1
    i,j=0,1
    while j<len(array)-1:
        if array[i]!=array[j]:
            i+=1
            array[i],array[j]=array[j],array[i]
        j+=1
    return i+1
j=[1,1,2,3,4,4,5]
print(j)
print(r_d(j))
print(j)



