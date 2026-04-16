class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count = (len(b) + len(a) - 1) // len(a)
        
        extended_a = a * count
        
        if b in extended_a:
            return count
        
        if b in (extended_a + a):
            return count + 1
            

if __name__ == "__main__":
    a = "abcd"
    b = "cdabcdab"

    print(Solution().repeatedStringMatch(a,b))