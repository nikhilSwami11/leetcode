class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        dsu = DSU(n)
        ans = []

        for u, v in requests:
            root_u = dsu.find(u)
            root_v = dsu.find(v)

            if root_u == root_v:
                ans.append(True)

            else:
                is_valid = True

                for x, y in restrictions:
                    root_x = dsu.find(x)
                    root_y = dsu.find(y)

                    if (root_x == root_u and root_y == root_v) or (root_x == root_v and root_y == root_u):
                        is_valid = False
                        break

                if is_valid:
                    dsu.union(root_u, root_v)
                    ans.append(True)
                else:
                    ans.append(False)

        return ans
    
n = 3
restrictions = [[0,1]]
requests = [[0,2],[2,1]]

print(Solution().friendRequests(n,restrictions,requests))