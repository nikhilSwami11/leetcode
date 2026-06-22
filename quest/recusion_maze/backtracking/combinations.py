from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, combination_set: List[int]):
            if len(combination_set) == k:
                ans.append(list(combination_set))
                return
            else:
                for i in range(start, n+1):
                    combination_set.append(i)
                    backtrack(i+1, combination_set)
                    combination_set.pop()
            
        backtrack(1,[])
        return ans
        

n = 5
k = 3
print(Solution().combine(n,k))