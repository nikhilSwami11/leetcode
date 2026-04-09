from collections import deque


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        q = deque()

        for i, ticket in enumerate(tickets):
            q.append([ticket, i==k])

        time = 0
        while q:
            time+=1
            val = q.popleft()
            val[0] -= 1

            if val[0]==0 and val[1] is True:
                return time
            if val[0] > 0:
                q.append(val)
        
        return time
    
tickets = [2,3,2]
k = 2

print(Solution().timeRequiredToBuy(tickets,k))

        