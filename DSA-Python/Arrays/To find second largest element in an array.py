def s_lar(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    for i in nums:
        if i>largest:
            s_largest=largest
            largest=i
    return s_largest
o=[2,43,24,54,676,43,65]
print(o)
print(s_lar(o))