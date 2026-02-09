class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = COLS = 9
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        squaremap = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowmap[r] or
                    board[r][c] in colmap[c] or
                    board[r][c] in squaremap[(r // 3, c // 3)]):
                    return False
                colmap[c].add(board[r][c])
                rowmap[r].add(board[r][c])
                squaremap[(r // 3, c // 3)].add(board[r][c])
        return True
                
