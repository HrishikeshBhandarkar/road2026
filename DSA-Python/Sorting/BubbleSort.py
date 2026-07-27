def bub_sort(list1):
    n=(len(list1))
    for i in range(n):
        swap=False #This line is to optimise the code if the array passed is already sorted
        for j in range(n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                swap=True
        if swap==False:
            return
f=[3,-1,55,34,56,32,43,44332,42,1,4]
print(f)
bub_sort(f)
print(f)
