class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)
        path = []
        while left < right and top < bot:
            for c in range(left, right):
                path.append(matrix[top][c])
            top += 1
            for r in range(top, bot):
                path.append(matrix[r][right - 1])
            right -= 1

            if not (left < right and top < bot):
                break
                
            for c in range(right - 1, left - 1, -1):
                path.append(matrix[bot - 1][c])
            bot -= 1
            for r in range(bot - 1, top - 1, -1):
                path.append(matrix[r][left])
            left += 1
        return path
