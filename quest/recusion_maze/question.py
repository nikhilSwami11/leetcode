from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        i = 0
        n = len(arr)
        curr_sum = 0
        count = 0
        while i < n:
            curr_sum += arr[i]
            if (i - start + 1) == k:
                if curr_sum >= k * threshold:
                    print(curr_sum)
                    print(arr[start],arr[i])
                    count+=1
                curr_sum -= arr[start]
                start+=1
            i +=1
        return count


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(Solution().maxSatisfied(customers,grumpy,minutes))