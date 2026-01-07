from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        log_stack = []
        prev_time =0

        for log in logs:
            id, type, timestamp = log.split(':')
            id, timestamp = int(id) , int(timestamp)

            if type == 'start':
                if log_stack:
                    ans[log_stack[-1]] += timestamp - prev_time
                log_stack.append(id)
                prev_time = timestamp
            else:
                top_id = log_stack.pop()
                ans[top_id] += timestamp - prev_time + 1
                prev_time = timestamp+1
        return ans


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(Solution().exclusiveTime(n,logs))