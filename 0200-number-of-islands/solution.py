class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0

        def dfs(r, c) -> int:
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == "0"):
                return 0
            # we are at valid square
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                count += dfs(r, c)
        return count

