from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                jumps += 1
                curr_end = farthest

                if curr_end >= len(nums) - 1:
                    break

        return jumps

input = [7,6,4,3,1]
ans = Solution().jump(input)

print (ans)
