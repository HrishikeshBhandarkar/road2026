def largest(nums):
    maxi=nums[0]
    for i in nums:
        maxi=max(maxi,i)
    return maxi
h=[-98,948,3728,48,243,-8]
print(h)
print(largest(h))