class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxCount = 0
        visited = set()
        def dfs(r, c):
            if (min(r,c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r,c) in visited):
                return 0
            visited.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r, c + 1) +
                        dfs(r - 1, c) +
                        dfs(r, c - 1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxCount = max(maxCount, dfs(row, col))
        return maxCount
