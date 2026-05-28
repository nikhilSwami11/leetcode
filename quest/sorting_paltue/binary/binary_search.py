from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n-1
        while left<right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else: left = mid +1
        return -1

if __name__ == "__main__":
    # Todo
    nums = [-1,0,3,5,9,12]
    target = 2
    print(Solution().search(nums, target))
    