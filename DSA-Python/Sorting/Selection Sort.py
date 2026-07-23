def selec(list1):
    for i in range(len(list1)):
        min_id=i
        av=list1[i]
        for j in range (i+1,len(list1)):
            if list1[j]<list1[min_id]:
                min_id=j
        if min_id!=i:
            list1[i],list1[min_id]=list1[min_id],list1[i]
e=[4,2,1,44,24,6443,2,322,34,45]
print(e)
selec(e)
print(e)