from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
       nums.sort()

       min_val = float('inf')

       for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left< right:
                net = nums[i] + nums[left] + nums[right]
                if abs(target - net) < abs(target - min_val):
                    min_val = net
                if net == target:
                    return 0
                elif net > target:
                    right -=1
                else:
                    left +=1
       return min_val

nums = [-1,2,1,-4], target = 1
