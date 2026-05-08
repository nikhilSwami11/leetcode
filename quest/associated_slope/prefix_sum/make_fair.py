from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_even = sum(nums[0::2])
        right_odd = sum(nums[1::2])

        left_even = 0
        left_odd = 0

        ans = 0

        for i, val in enumerate(nums):
            if i%2== 0:
                right_even -= val
            else :
                right_odd -= val

            if left_odd + right_even == left_even + right_odd:
                ans+=1

            if i%2== 0:
                left_even += val
            else:
                left_odd += val 
        return ans
    

    # 1 2 3 4  5  6  7  8  9 
    # 1 2 4 6  9  12 16 20 25  
    
if __name__ == "__main__":
    nums = [6,1,7,4,1]
    print(Solution().waysToMakeFair(nums))