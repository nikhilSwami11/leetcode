class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        pattern = s + "#" + rev_s

        n = len(pattern)

        prev_len, i = 0,1
        lps = [0]*n

        while i< n:
            if pattern[i] == pattern[prev_len]:
                prev_len +=1
                lps[i] = prev_len
                i+=1
            elif prev_len ==0:
                lps[i] = 0
                i+=1
            else:
                prev_len = lps[prev_len-1]

        longest_suffix_length = lps[-1]
        return s[longest_suffix_length:][::-1] + s


s = "aacecaaa"
print(Solution().shortestPalindrome())