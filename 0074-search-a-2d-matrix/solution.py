class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else: #target poss in mid
                break
        if not (l <= r):
            return False
        left, right = 0, COLS - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[mid][middle]:
                left = middle + 1
            elif target < matrix[mid][middle]:
                right = middle - 1
            else:
                return True
        return False

