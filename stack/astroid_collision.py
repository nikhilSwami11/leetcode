from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # res = []

        # for a in asteroids:

        #     while res and a < 0 < res[-1]:
        #         if -a > res[-1]:
        #             res.pop()
        #             continue
        #         elif -a == res[-1]:
        #             res.pop()
        #         break
        #     else:
        #         res.append(a)

        # return res
        stack = []
        index = 0
        while index < len(asteroids):
   
            if(len(stack) == 0):
                stack.append(asteroids[index])
                index+=1
                continue
            else:
                if(stack[-1] > 0 and  asteroids[index] <0):
                    if(stack[-1] + asteroids[index] > 0):
                        if(asteroids[index] > 0):
                            stack.append(asteroids[index])
                        index +=1
                
                    elif (stack[-1] + asteroids[index] ==0):
                        stack.pop()
                        index+=1
                    else:
                        stack.pop()
                else:
                    stack.append(asteroids[index])
                    index+=1
            
        return stack

asteroids = [5,10,-5]
print(Solution().asteroidCollision(asteroids))