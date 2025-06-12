from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff =0
        for i in range(n):
            diff = nums[(i+1)%n] - nums[i%n]
            max_diff = max(abs(diff), max_diff)
        return max_diff


input = [1,2,4]
print(Solution().maxAdjacentDistance(input))