class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if rooms == []:
            return False
        
        st = [0]
        visitedRooms = {0}

        while st:
            room = st.pop()

            for key in rooms[room]:
                if key not in visitedRooms:
                    visitedRooms.add(key)
                    st.append(key)
        
        return len(visitedRooms) == len(rooms)



if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    rooms = [[1],[2],[3],[]]
    
    sol = Solution()
    print("Result:", sol.canVisitAllRooms(rooms))