import heapq


class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """

        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            max_val = -heapq.heappop(max_heap)
            others_sum = total_sum - max_val
            
            if max_val == 1 or others_sum == 1:
                return True
            
            if max_val < others_sum or others_sum == 0 or max_val % others_sum == 0:
                return False
            
            new_val = max_val % others_sum
            
            total_sum = others_sum + new_val
            heapq.heappush(max_heap, -new_val)

        
target = [9,3,5]
print(Solution().isPossible(target))