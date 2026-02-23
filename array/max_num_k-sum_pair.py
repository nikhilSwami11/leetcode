from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mp = {}
        count =0
        # Store count of each number in nums array
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        
        for key in mp:
            diff = k - key
            print(key, diff)
            if diff in mp and diff !=0:
                combinations = min(mp[key], mp[diff])
                if(key == diff):
                    combinations = 2*(combinations//2)
                count +=combinations
    
        return count//2
            
        
# INPUT
nums = [3,1,3,4,3]
k = 6

print(Solution().maxOperations(nums,k))