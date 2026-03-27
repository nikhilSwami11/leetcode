


class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = (len(mat[0]))
        k %= n

        for row in mat:
                for i in range(n):
                    if row[i] != row[(i+k)%n]:
                        return False
                    
                    
        return True


mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2

print(Solution().areSimilar(mat, k))





        