def rotate(nums):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    for t in range(n):
        nums[t].reverse()
nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(nums)
rotate(nums)
print(nums)