class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIM = len(grid)
        queue = deque()
        visited = set()
        queue.append((0,0,1))
        visited.add((0,0))
        if grid[DIM - 1][DIM - 1] == 1 or grid[0][0] == 1:
            return -1
        def bfs(r, c):
            while queue:
                for i in range(len(queue)):
                    r, c, path = queue.popleft()
                    if r == DIM - 1 and c == DIM - 1:
                        return path
                    directions = [[-1,0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
                    for dr, dc in directions:
                        if (min(r + dr, c + dc) < 0 or
                            max(r + dr, c + dc) == DIM or
                            grid[r + dr][c + dc] == 1 or
                            (r + dr, c + dc) in visited):
                            continue
                        queue.append((r + dr, c + dc, path + 1))
                        visited.add((r + dr, c + dc))
            return -1
        
        return bfs(0,0)
