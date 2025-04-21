from itertools import accumulate
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        end = len(prefix_sum)-1
        for i, _ in enumerate(prefix_sum):
            if prefix_sum[end] - prefix_sum[i] == (prefix_sum[i-1] if i>0 else 0):
                return i
        return -1
        

nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))