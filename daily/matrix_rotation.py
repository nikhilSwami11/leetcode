class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)
        c0 = c90 = c180 = c270 = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    c0 = False
                if mat[r][c] != target[c][n - 1 - r]:
                    c90 = False
                if mat[r][c] != target[n - 1 - r][n - 1 - c]:
                    c180 = False
                if mat[r][c] != target[n - 1 - c][r]:
                    c270 = False
                    
        return c0 or c90 or c180 or c270


mat = [[0,1],[1,0]], target = [[1,0],[0,1]]

print(Solution().areSimilar(mat, target))