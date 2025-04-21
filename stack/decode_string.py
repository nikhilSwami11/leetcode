class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        for value in s:
            if(value != ']'):
                stack.append(value)
            else:
                # base string 
                s = ""
                # popping stack until the opening bracket
                while stack and stack[-1] !='[':
                    s = stack.pop() + s
                # popping the opening bracket
                stack.pop()
                # getting the stack string
                numString = ""
                while stack and stack[-1].isdigit():
                    numString = stack.pop() +  numString
                nums = int(numString)
                print(nums)
                newString = ""
                while(nums!=0):
                    nums -=1
                    newString += s 
                stack.extend(newString)
        return "".join(stack)

s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))