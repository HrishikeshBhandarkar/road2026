#We can use several methods to do this, one with slicing but as slicing is only present in python i will write another method as well
def rr(array):
    n=len(array)
    array[:]=[(array[n-1])]+array[0:n-1] # array[n-1] gives a single number so it is treated as int not list, u cannot wrap it inside list() function as python expects something it can loop over say a string or a tuple ar another list for that matter so we wrap it around "[]" to make a single element a list
#Second way is 

def rr2(array):
    n=len(array)
    temp=array[n-1]
    for i in range(n-2,-1,-1):
        array[i+1]=array[i]
    array[0]=temp

i=[4,5,3,2,345,5]
o=[8,4,32,33,21,3]
print(i)
rr(i)
print(i)
print(o)
rr2(o)
print(o)