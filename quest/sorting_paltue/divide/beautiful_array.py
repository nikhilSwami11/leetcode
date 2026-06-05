from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n ==1 :
         return [1]

        odd_base = self.beautifulArray((n+1)//2)
        even_base = self.beautifulArray((n)//2)

        odd_part = [2*x -1 for x in odd_base]
        even_part = [2*x for x in even_base]

        return odd_part+even_part


print(Solution().beautifulArray(4))