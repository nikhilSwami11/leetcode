from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        all_combinations = []

        def backtrack(combination: List[str]):
            if len(all_combinations) == k:
                return

            if len(combination)==n:
                all_combinations.append("".join(combination))
                return
            else:
                for c in ['a','b','c']:
                    if not combination or combination[-1] != c:
                        combination.append(c)
                        backtrack(combination)
                        combination.pop()

        backtrack([])
        if len(all_combinations) < k:
            return ""
        else: return all_combinations[k-1]
                
        
n = 3
k = 9
print(Solution().getHappyString(n,k))