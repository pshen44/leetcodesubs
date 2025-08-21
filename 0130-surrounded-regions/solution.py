class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visit = set()
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit:
                return
            if board[r][c] != "O":
                return
            
            board[r][c] = "S"
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            visit.remove((r,c))
            return

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr == ROWS or c + dc == COLS):
                            dfs(r, c)
        print(board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


