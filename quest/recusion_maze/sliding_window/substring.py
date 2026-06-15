class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc_set = {}
        start = 0
        n = len(s)
        total_substring = 0
        i = 0
        for i in range(n):
            abc_set[s[i]] = abc_set.get(s[i], 0) + 1

            while len(abc_set) == 3:
                total_substring += n - i
                abc_set[s[start]] -= 1
            
                if abc_set[s[start]] == 0:
                    del abc_set[s[start]]
                start += 1
        return total_substring


s = "aaacb"
print(Solution().numberOfSubstrings(s))