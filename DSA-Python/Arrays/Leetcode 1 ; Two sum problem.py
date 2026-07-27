def trs(nums,target):
    hash=dict()
    n=len(nums)
    for i in range(n):
        remaining=target-nums[i]
        if remaining in hash:
            return [hash[remaining],i]
        hash[nums[i]]=i
o=[5,9,1,2,4,15,6,3]
print(o)
p=trs(o,13)
print(p)