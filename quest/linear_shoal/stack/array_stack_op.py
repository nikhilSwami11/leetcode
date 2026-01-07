from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        prev = 0 
    
        for num in target:
            gaps = num - prev - 1
            ans += ["Push", "Pop"] * gaps
            ans.append("Push")
            prev = num
        return ans

target = [3]
print(Solution().buildArray(target, 3))