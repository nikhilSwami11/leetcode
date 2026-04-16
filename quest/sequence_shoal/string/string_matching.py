class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        double_string = s+s
        print(double_string)
        n = len(s)
        for i in range(1,n):
            if double_string[i:i+n] == s:
                return True
        return False

print(Solution().repeatedSubstringPattern("bb"))
