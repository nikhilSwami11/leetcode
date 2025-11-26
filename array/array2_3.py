from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = {}
        count = 0
        for i in range(n):
            mp[i+1] = 0
    
        print(count)
        for val in nums:
            if val in mp:
                mp[val]+=1
        output = []

        print(mp)
        for key in mp:
            if mp[key]==0:
                output.append(key)
        
        return output
    
input = [4,3,2,7,8,2,3,1]
ans = Solution().findDisappearedNumbers(input)

print (ans)