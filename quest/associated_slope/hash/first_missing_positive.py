from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = {} 
        for val in nums:
            if val > 0:
                mp[val] = 1
        
        for possible in range(1,len(mp)+2):
            if possible not in mp:
                return possible
        return 1    

if __name__ == "__main__":
    nums = [1,2,0]
    print(Solution().firstMissingPositive(nums))

