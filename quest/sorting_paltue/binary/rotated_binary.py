from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[left]:
                # means we are in the second slope
                if nums[mid] < target and nums[right] >= target:
                    # search in right
                    left = mid + 1
                else : right = mid -1 
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid -1
                else: left = mid+1
        return -1

        


nums = [4,5,6,7,0,1,2]
target = 0
Solution().search()