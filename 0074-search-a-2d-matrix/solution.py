class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            middle = (top + bot) // 2
            if target < matrix[middle][0]:
                bot = middle - 1
            elif target >matrix[middle][-1]:
                top = middle + 1
            else:
                break

        if not (top <= bot):
            return False

        middle = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[middle][mid]:
                r = mid - 1
            elif target > matrix[middle][mid]:
                l = mid + 1
            else:
                return True
        return False

            

        
