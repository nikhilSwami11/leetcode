from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        vowel_count = 0
        for i in range(k):
            if(s[i] in ['a','e','i','o', 'u']):
                vowel_count +=1
        max_count = vowel_count
        for i in range(k,n):
            if(self.isVowel(s[i])):
                vowel_count+=1
            if(self.isVowel(s[i-k])):
                vowel_count-=1
            max_count = max(max_count,vowel_count)
        return max_count

    def isVowel(self, s: str) -> bool:
        return s in ['a','e','i','o', 'u']


# INPUT
s = "leetcode"
k = 3

print(Solution().maxVowels(s,k))

1,2,3,4,5