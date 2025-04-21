from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s =0
        for i in range(k):
            s += nums[i]
        ans = s/k

        for i in range(k,n):
            s -=nums[i-k]
            s+= nums[i]
            if(s/k > ans):
                ans = s/k
        return ans


# INPUT
nums =[1,12,-5,-6,50,3]
k = 4

print(Solution().findMaxAverage(nums,k))

