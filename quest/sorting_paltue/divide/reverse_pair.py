from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1, -1,-1):
                if 2*nums[i]<nums[j]:
                    count+=1
        
        return count

nums = [2,4,3,5,1]
print(Solution().reversePairs(nums))

