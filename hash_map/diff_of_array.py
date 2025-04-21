from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        mp = {}
        mpx = {}
        mp1 = {}
        mp2 = {}

        for val in nums1:
            mp[val] = True
        for val in nums2:
            mpx[val] = True

        for val in nums2:
            if(val not in mp):
                mp2[val] = True
        
        for val in nums1:
            if(val not in mpx):
                mp1[val] = True

        return [list(mp1.keys()), list(mp2.keys())]

        pass

nums1 =[-68,-80,-19,-94,82,21,-43]
nums2 =[-63]

print(Solution().findDifference(nums1,nums2))