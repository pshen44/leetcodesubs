class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (r + l) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        if not (l <= r):
            return False
        mid = (l + r) // 2
        left, right = 0, len(matrix[mid]) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[mid][middle]:
                left = middle + 1
            elif target < matrix[mid][middle]:
                right = middle - 1
            else:
                return True
        return False

