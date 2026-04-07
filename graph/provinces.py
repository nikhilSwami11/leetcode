class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        unvisited = {x for x in range(len(isConnected))}
        provinces = 0

        while unvisited:
            starting_node = unvisited.pop()
            # bfs
            st = [starting_node]
            while st:
                node = st.pop()

                for neighbor, is_linked in enumerate(isConnected[node]):
                    if is_linked==1 and neighbor in unvisited:
                        unvisited.remove(neighbor)
                        st.append(neighbor)

            provinces+=1
        return provinces


if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]

    sol = Solution()
    print("Result" , sol.findCircleNum(isConnected)) 
