class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        res = n
        for s in sandwiches:
            c = 0
            while c < n and q[0] != s:
                cur = q.popleft()
                q.append(cur)
                c += 1
            
            if q[0] == s:
                q.popleft()
                res -= 1
            else:
                break
        return res
