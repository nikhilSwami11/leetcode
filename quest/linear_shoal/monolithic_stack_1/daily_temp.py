from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        st = []
        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                index = st.pop()
                ans[index] = i - index
            st.append(i)
        return ans


temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
