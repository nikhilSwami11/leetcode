from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums)<3):
            return False
        
        first = float('inf')
        second = float('inf')

        for i in range(len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i] :
                second = nums[i]
            else:
                return True
        return False

nums = [2,1,5,0,4,6]
print(Solution().increasingTriplet(nums))