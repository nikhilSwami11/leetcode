from typing import List

# The idea is that we take a start index and an end index
# now calculate the area. We move the index which has less height.

class Solution:
    ### BRUTE FORCE SOLUTION
    # def maxArea(self, height: List[int]) -> int:
    #     n = len(height)
    #     max_area =0

    #     for i in range(n):
    #         flag = 0
    #         for j in range(n-1,0,-1):
    #             if(i==j):
    #                 flag =1
    #                 break
    #             h = min(height[i], height[j])
    #             w = j-i
    #             print(h,w)
    #             area = w*h
    #             if(area>max_area):
    #                 max_area = area
    #         if(flag==1):
    #             break
    #     return max_area
    
    # OPTIMIZED
     def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area =0
        start =0
        end =n-1

        while(start<end):
            h = min(height[start], height[end])
            w = end - start
            area = h*w
            max_area = max(area, max_area)
            if(height[start]>= height[end]):
                end -=1
            else:
                start+=1
        return max_area



height = [1,8,6,2,5,4,8,3,7]        
s = Solution()
print(s.maxArea(height=height))

