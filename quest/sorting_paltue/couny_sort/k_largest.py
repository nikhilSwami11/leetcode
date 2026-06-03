import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_min_heap = []

        for num in nums:
            if len(k_min_heap) < k:
                heapq.heappush(k_min_heap, num)

            else:
                if k_min_heap[0] < num:
                    heapq.heappop(k_min_heap)
                    heapq.heappush(k_min_heap,num)            
        return k_min_heap[0]
        

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums,k))