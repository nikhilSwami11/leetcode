from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_array = [0]*len(gain)
        for i in range(len(gain)):
            if i==0:
                sum_array[i] = gain[i]
            else:
                sum_array[i] = sum_array[i-1]+gain[i]
        return max(0, max(sum_array))


gain =  [-4,-3,-2,-1,4,3,2]

print(Solution().largestAltitude(gain))