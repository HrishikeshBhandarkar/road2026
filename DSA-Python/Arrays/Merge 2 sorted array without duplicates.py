def m_awd(array1,array2):
    o,p=len(array1),len(array2)
    i,j=0,0
    result=[]
    while i<o and j<p:
        if array1[i]<=array2[j]:
            if len(result)==0:
                result.append(array1[i])
            elif result[-1]!=array1[i]:
                result.append(array1[i])
            i+=1
        else:
            if len(result)==0:
                result.append(array2[j])
            elif result[-1]!=array2[j]:
                result.append(array2[j])
            j+=1
    if i<o:
        while i<o:
            if result[-1]!=array1[i]:
                result.append(array1[i])
            i+=1
    if j<p:
        while j<p:
            if result[-1]!=array2[j]:
                result.append(array2[j])
            j+=1
    return result
o=[1,2,3,3,4,5,6,6]
p=[6,7,8,8,9,10,10]
print(o,"\n",p)
r=m_awd(o,p)
print(r)

