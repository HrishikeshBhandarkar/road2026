class Solution:
    def resultArray(self, nums):
        re1 = []
        re2 = []
        re1.append(nums[0])
        re2.append(nums[1])
        for i in range(2, len(nums)):
            c = nums[i]
            if re1[-1]>re2[-1]:
                re1.append(nums[i])
            else: re2.append(nums[i])
        return re1 + re2

if __name__ == "__main__":
    u = [5,4,3,8]
    i = Solution().resultArray(u)
    print(i)
