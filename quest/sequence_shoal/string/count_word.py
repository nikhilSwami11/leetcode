class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count_cap = 0
        count_small = 0
       
        for i in range(1,len(word)):
            if ord(word[i])>= ord('A') and ord(word[i])<= ord('Z') :
                count_cap += 1
            else: count_small+= 1
        
        if ord(word[0])>= ord('A') and ord(word[0])<= ord('Z'):
            if count_cap == len(word)-1 or count_small == len(word) -1:
                return True
            else: return False

        elif count_small == len(word)-1:
            return True
        return False
print(Solution().detectCapitalUse("FlaG"))