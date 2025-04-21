class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mp1 = {}
        mp2 = {}

        for value in word1:
            if value in mp1:
                mp1[value] +=1
            else:
                mp1[value]=1
        for value in word2:
            if value in mp2:
                mp2[value] +=1
            else:
                mp2[value]=1

        l1 = list(mp1.values())
        l2 = list(mp2.values())
        l1.sort()
        l2.sort()

        l3 = list(mp1.keys())
        l4 = list(mp2.keys())
        l3.sort()
        l4.sort()

        if(l1==l2 and l3==l4):
            return True
        return False

word1  = "uau"
word2 = "ssx"
print(Solution().closeStrings(word1,word2))