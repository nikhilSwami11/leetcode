from typing import List


class Solution(object):
    def largestRectangleArea(self, heights: List[int]):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)
        st = [-1]

        max_area = -1
        print(heights)

        for i in range(len(heights)):
            while st[-1] != -1 and heights[i] < heights[st[-1]]:
                curr_index = st.pop()
                width = i - st[-1] - 1
                max_area = max(heights[curr_index]*width, max_area)
            st.append(i)
                        
        heights.pop()
        return max_area
    
if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print("Result:", Solution().largestRectangleArea(heights))
                