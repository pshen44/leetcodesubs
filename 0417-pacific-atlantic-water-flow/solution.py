class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    if (r + dr == ROWS or c + dc == COLS or
                        min(r + dr, c + dc) < 0 or
                        heights[r + dr][c + dc] < heights[r][c] or
                        ocean[r + dr][c + dc]):
                        continue
                    q.append((r + dr, c + dc))
        
        pacific = []
        atlantic = []
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        for c in range(COLS):
            atlantic.append((ROWS - 1, c))
            pacific.append((0, c))
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res


                    
        
