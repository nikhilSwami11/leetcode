class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire =[]
        n  = len(senate)

        for i,s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)
            if r > d:
                dire.append(d + n)
            else:
                radiant.append(r+n)
            
        return "Radiant" if radiant else "Dire"
    
    
senate = "DDRRR"
ans = Solution().predictPartyVictory(senate)
print(ans)