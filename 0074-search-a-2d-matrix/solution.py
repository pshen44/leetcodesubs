class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                s, e = 0, len(matrix[mid]) - 1
                while s <= e:
                    print(s,e)
                    middle = (s + e) // 2
                    print(matrix[mid][middle])
                    if target > matrix[mid][middle]:
                        s = middle + 1
                    elif target < matrix[mid][middle]:
                        e = middle - 1
                    else:
                        return True
                return False
                    
        return False
