class Solution(object):
    def checkStrings(self, s1, s2):

        s11mp = {}
        s12mp = {}
        s21mp = {}
        s22mp = {}
        for i, val in enumerate(s1):
            if i%2 == 0:
                if val in s11mp:
                    s11mp[val] +=1
                else:
                    s11mp[val] = 1
            else:
                if val in s12mp:
                    s12mp[val] +=1
                else:
                    s12mp[val] =1
            
        for i, val in enumerate(s2):
            if i%2 == 0:
                if val in s21mp:
                    s21mp[val] +=1
                else:
                    s21mp[val] = 1
            else:
                if val in s22mp:
                    s22mp[val] +=1
                else:
                    s22mp[val] =1

        print(s11mp, s21mp)
        print(s12mp, s22mp)
        return (s11mp == s21mp) & (s12mp == s22mp)
        


s1 = "abcdba"
s2 = "cabdab"
print(Solution().checkStrings(s1,s2))