from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = -1

        while (end < len(nums)-1):
            end+=1
            if(nums[end] == 0):
                k-=1
            if(k<0):
                start+=1
                if(nums[start]==0):
                    k+=1
            

        return end - start
                  

nums =  [0,0,0,1,1,1,1,0]
k = 0

print(Solution().longestOnes(nums,k))