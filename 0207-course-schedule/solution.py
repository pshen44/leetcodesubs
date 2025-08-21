class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        visit = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
