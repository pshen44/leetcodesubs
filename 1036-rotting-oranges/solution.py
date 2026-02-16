class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        minutes = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(ROWS) and
                    c in range(COLS) and
                    grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1
                        



