from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = {}
        for val in arr:
            if val in mp:
                mp[val] +=1
            else:
                mp[val]=1
        
        l = list(mp.values())
        my_set = set(l)

        if len(my_set)==len(l):
            return True
        return False
        

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(Solution().uniqueOccurrences(arr))