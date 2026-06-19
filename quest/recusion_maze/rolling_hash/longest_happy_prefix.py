class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]*n

        length, i =0, 1
        while i < n:
            if s[i] == s[length]:
                length +=1
                lps[i] = length
                i+=1
            elif length ==0:
                lps[i] = 0
                i+=1
            else:
                length = lps[length-1]

        return s[n-lps[-1]:]

s = "ababab"
print(Solution().longestPrefix(s))