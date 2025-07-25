from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1,n):
            if prices[i]-prices[i-1] >= 0:
                profit+= prices[i]-prices[i-1]
        
        return profit

input = [7,6,4,3,1]
ans = Solution().maxProfit(input)

print (ans)