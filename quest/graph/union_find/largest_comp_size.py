from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def getPrimeFactors(n : int):
            factor = set()
            if n % 2 == 0:
                factor.add(2)
                while n %2 ==0:
                    n //= 2

            i = 3
            while i*i <=n:
                if n % i == 0:
                    factor.add(i)
                    while n % i ==0:
                        n //= i
                i += 2
            if i > 1:
                factor.add(i)
            return factor
        mp = {}

        