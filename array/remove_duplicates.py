from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k =2
        for i in range (2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k

        


input = [1,1,1,2,2,3]
ans = Solution().removeDuplicates(input)

print (ans)