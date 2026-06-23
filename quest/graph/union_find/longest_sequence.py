from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_count = 0

        for num in s:
            if (num -1) not in s:
                curr = num
                count = 0
                while curr in s:
                    count += 1
                    curr+=1
                max_count = max(count,max_count)
        return max_count
    
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))

