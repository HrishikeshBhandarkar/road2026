def count_ones(array):
# I somehow managed to make an easy problem to take TimeComplexity of O(N**2) 
# While tackling problems its best to think like a computer that things of what to do with element it found at the time and not to worry about other elements
    n=len(array)
    count=None
    x=[0]
    for i in range(n):
        if array[i]==1:
            count=1
            j=i+1
            while j<n:
                if array[j]==1:
                    count+=1
                    j+=1
                else: break
            x.append(count)
    return max(x)
array=[1,0,1,0,1,1,1,1,0,1]
print(array)
e=count_ones(array)
print(e)
                
def count_one2(array):
    current_streak=0
    max_streak=0
    for i in array   :
        if i==1:
            current_streak+=1
            if current_streak>max_streak:
                max_streak=current_streak
        else:
            current_streak=0
    return max_streak

array=[1,0,1,0,1,1,1,1,0,1]
print(array)
e=count_one2(array)
print(e)     
