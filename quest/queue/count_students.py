from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        q = deque(students)
        counter = 0
        
        while counter < len(q):
            student = q.popleft()
            if student == sandwiches[0]:
                sandwiches.pop(0)
                counter =0
            else:
                q.append(student)
                counter +=1
        return len(q)

students = [1,1,0,0]
sandwiches = [0,1,0,1]

print(Solution().countStudents(students, sandwiches))