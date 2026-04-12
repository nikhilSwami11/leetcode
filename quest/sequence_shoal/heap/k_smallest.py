import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []
        n = min(len(nums1),k)
        for i in range(n):
            min_heap.append((nums1[i]+nums2[0],i,0))
        heapq.heapify(min_heap)

        results = []
        while k:
           curr_sum, i, j = heapq.heappop(min_heap)
           results.append([nums1[i],nums2[j]])
           if (j+1) < len(nums2):
            heapq.heappush(min_heap,(nums1[i]+nums2[j+1], i, j+1))
           k -=1
        
        return results

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print(Solution().kSmallestPairs(nums1, nums2, k)) 