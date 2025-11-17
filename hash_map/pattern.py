from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        map = {}

        if len(words) != len(pattern):
            return False 
    
        for c, word in zip(pattern, words):
            if word in map.values():
                if c in map and map[c] == word:
                    continue
                else: return False
            elif c not in map:
                map[c] = word
            else: return False

        return True


pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern,s))