def merge_arry(left,right):
    result=[]
    o,p=len(left),len(right)
    i,j=0,0
    while i<o and j<p:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1
    if i<o:
        for k in range(i,o):
            result.append(left[k])
    if j<p:
        for k in range(j,p):
            result.append(right[k])
    return result
# x=[1,2,3,4]
# y=[4,5,6,7,8,9]
# print(x,"\n",y)
# print("Mergered list = ",merge_arry(x,y))

def merg_sort(arry):
    if len(arry)==1:
        return arry
    mid=len(arry)//2
    left_arry=arry[:mid]
    right_arry=arry[mid:]
    left=merg_sort(left_arry)
    right=merg_sort(right_arry)
    return merge_arry(left,right)

y=[9,33454,239,213,44,2334,2134,2484,23,123443,3]
print(y)
print("Sorted array = ",merg_sort(y))

