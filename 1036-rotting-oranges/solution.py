class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))
        direc = [[1,0], [0,1], [-1,0], [0,-1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direc:
                    if (r + dr == ROWS or c + dc == COLS or
                        min(r + dr, c + dc) < 0):
                        continue
                    if grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
            

