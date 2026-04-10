import heapq
from typing import List


class Solution(object):
    def lastStoneWeight(self, stones : List[int]):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap_max = [-x for x in stones]
        heapq.heapify(heap_max)
        
        while len(heap_max) > 1:
            first = heapq.heappop(heap_max)
            second = heapq.heappop(heap_max)
            diff = first - second
            if diff !=0:
                heapq.heappush(heap_max, diff)
        return 0 if not heap_max else -heap_max[0]

            

stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))