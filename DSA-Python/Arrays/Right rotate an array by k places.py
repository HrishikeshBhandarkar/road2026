def rrk(nums,k):
    
    n=len(nums)
    k=k%n
    nums[:]=nums[n-k:]+nums[:n-k]

# Now without using slicing, we use the logic of reversing an array to solve this 

def rev(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def rrkp(nums,k):
    n=len(nums)
    k=k%n
    rev(nums,n-k,n-1)

    rev(nums,0,n-k-1)

    rev(nums,0,n-1)
print("Execution of first logic [k=3] = ")
o=[90,94,43,54,34,23,54,554]
print(o)
rrk(o,3)
print(o)
j=[56,54,3,456,43,45,5332,46]
print("Executiion of second logic with k set as 3 again = ")
print(j)
rrkp(j,3)
print(j)