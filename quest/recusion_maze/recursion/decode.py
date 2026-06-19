class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == "]":
                pattern = ""
                while st[-1] != "[":
                    pattern = st.pop() + pattern
                st.pop()

                num_str = ""
                while st and st[-1].isdigit():
                    num_str = st.pop() + num_str
                num = int(num_str)
                st.append(pattern * num)
            else :
                st.append(c)

        return "".join(st)
    
s = "3[a]2[bc]"
print(Solution().decodeString(s))
            
