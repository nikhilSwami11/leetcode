from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = arr
        nums.sort()

        ans = []
        min_diff = float('inf')
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] < min_diff:
                ans = []
                min_diff = nums[i] - nums[i-1]
            if nums[i] - nums[i-1] == min_diff:
                ans.append([nums[i-1], nums[i]])
        return ans
    
print(Solution().minimumAbsDifference([1,2,3]))