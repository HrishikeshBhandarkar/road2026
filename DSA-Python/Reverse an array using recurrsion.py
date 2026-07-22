def rev(list1, list2):
    if len(list1) == 0:
        return list2
    else: 
        e = list1.pop()
        list2.append(e)
        return rev(list1, list2) 
y=[3,4,5,6,7,8,9,10]
z=y.copy()
o=[]
print(rev(y,o))
print(y)#Thhis destroys the original list tho so i will just make a copy of this 
print(z)

def fr(list1,left,right):#This will againn destroy the original array but in this u can reverse a particular part of the array using the pointers left and right
    if left==right or left>right:
        return list1
    else:
        list1[left],list1[right]=list1[right],list1[left]
        left+=1
        right-=1
        return fr(list1,left,right)
r=len(z)-1
print(fr(z,0,r))

#Now using while loop
def wrev(list1,left,right):
    while left<right:
        list1[left],list1[right]=list1[right],list1[left]
        left+=1
        right-=1
i=[3,6,7,8,9,10,88]
wrev(i,2,5)
print(i)