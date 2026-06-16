class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        start = 0
        max_possible = 1
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1

            if i - start + 1- max(mp.values()) > k :
                mp[s[start]] -=1
                if mp[s[start]] == 0:
                    del mp[s[start]]
                start +=1

            max_possible = max(i - start + 1,max_possible)
        return max_possible


s = "ABAB"
k = 2

print(Solution().characterReplacement(s,k))