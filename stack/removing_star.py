class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for value in s:
            if(value =="*"):
                stack.pop()
            else: 
                stack.append(value)
        
        ans = ""
        for val in stack:
            ans+= val
        return ans
        

s = "leet**cod*e"
print(Solution().removeStars(s))