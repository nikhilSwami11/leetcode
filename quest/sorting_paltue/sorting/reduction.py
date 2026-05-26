from typing import List



class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        steps = 0
        for i in range(n-1, 0,-1):
            if nums[i] != nums[i-1]:
                # nums[i] is largest
                count = n - i
                print(count)
                steps += count
        return steps


if __name__ == "__main__":
    nums = [1,1,2,2,3]
    print(Solution().reductionOperations(nums))






        
        
