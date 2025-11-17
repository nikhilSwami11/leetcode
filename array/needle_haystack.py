from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            needle_length = len(needle) 
            haystack_length = len(haystack)
            index = 0

            while index < haystack_length - needle_length + 1:
                if needle == haystack[index:index+needle_length]:
                        return index
                index += 1

            return -1
                        
                        
            

needle = "leeto"
haystack = "leetcode"
ans = Solution().strStr(haystack, needle)

print (ans)
