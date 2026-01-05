
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        ans = prices.copy()
        
        for i in range(len(prices)):
            if len(st)==0 or prices[i] > st[-1][1]:
                st.append([i,prices[i]])
        
            else: 
                while len(st) > 0 and st[-1][1] >= prices[i]:
                    price_tuple = st.pop()
                    new_price = prices[price_tuple[0]] - prices[i]
                    ans[price_tuple[0]] = new_price
                st.append([i,prices[i]])
        return ans

prices = [8,4,6,2,3]
print(Solution().finalPrices(prices))