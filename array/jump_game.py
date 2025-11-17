from typing import List


class Solution:
    def jump1(self, nums: List[int]) -> int:
        max_range = 0

        for i in range (len(nums)):
            if i > max_range:
                return False
            max_range = max(nums[i]+i, max_range)
            
        return True
            

        


        # while start < n:
        #     m = nums[start]
            
        #     jump_index = 0
        #     max_num = -1

        #     next_index = 1

        #     while next_index < m and next_index + start < n:
        #         possible_jumps = nums[start + next_index]


        #     for i in range(m):
        #         if i < n:
        #             num = nums[start+ i] - 1
        #             if (num > max_num):
        #                 jump_index = i
        #                 max_num = num
        #         else:
        #             return True
            
        #     start = jump_index
        
        return False
            




input = [3,2,1,0,4]
ans = Solution().jump1(input)

print (ans)
