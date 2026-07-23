def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        swap=False
        key = list1[i]
        j=i-1
        while j>=0 and list1[j]>key:
           
            list1[j+1]=list1[j]
            swap=True
            j-=1
        
        if swap==True:
            list1[j+1]=key

o=[9,43,-4,22,4243,232,134,21,34]
print(o)
insertion_sort(o)
print(o)
