from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""

        prefix_string = strs[0]
        prefix_length = len(prefix_string)

        for s in strs[1:]:
            while prefix_string != s[0:prefix_length]:
                prefix_length-=1
                if(prefix_length==0):
                    return ""
                prefix_string = prefix_string[0:prefix_length]
        
        return prefix_string
        

input = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(input))