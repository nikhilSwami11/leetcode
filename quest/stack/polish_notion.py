from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp_stack = []
        operations = ['+', '-', '*', '/']

        for val in tokens:
            if val in operations:
                val2 = temp_stack.pop()
                val1 = temp_stack.pop()
 
                ans = 0
                if val == '+':
                    ans = val1 + val2
                elif val == '-':
                    ans = val1 - val2
                elif val == '*':
                    ans = val1*val2
                elif val == '/':
                    ans = val1 / val2
                print
                temp_stack.append(int(ans))  
                 
            
            else:
                temp_stack.append(int(val))

        return temp_stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))