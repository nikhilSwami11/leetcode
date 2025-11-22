from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        for i in  range(len(citations)):
            remaining_research_paper = len(citations) - i
            if (citations[i] >= remaining_research_paper):
                return remaining_research_paper
        return 0


citations = [1,3,1]
ans = Solution().hIndex(citations)

print (ans)