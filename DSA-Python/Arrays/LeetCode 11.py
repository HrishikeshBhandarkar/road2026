from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            t = (r-l) * min(height[l],height[r])
            res = t if t>res else res
            if height[l] >= height[r]:
                r-=1
            else : l+=1
        return res

