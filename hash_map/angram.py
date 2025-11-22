class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        for character in t:
            if character not in map or map[character] == 0:
                return False
            map[character] -= 1
        return True


s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s,t))
