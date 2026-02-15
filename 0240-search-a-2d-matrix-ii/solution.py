class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #start at TL idx
        ROWS = len(matrix)
        COLS = len(matrix[0])
        r, c = 0, COLS - 1
        print(r,c, ROWS, COLS)
        while r < ROWS and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
                
        return False



