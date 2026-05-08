from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
    
        target = sum(nums)%p

        if target == 0:
            return 0
        
        curr_sum = 0
        last_seen = {0:-1}

        min_len = len(nums)

        for index, val in enumerate(nums):
            curr_sum = (curr_sum + val)%p

            needed_mod = (curr_sum - target + p)%p

            if needed_mod in last_seen:
                min_len = min(min_len, index - needed_mod)
            last_seen[curr_sum] = index
        
        if min_len < len(nums):
            return min_len
        else:
            return -1



nums = [3,1,4,2]
p = 6
print(Solution().minSubarray(nums, p))