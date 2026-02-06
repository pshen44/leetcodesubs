class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset, n, k):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i > n:
                return
            subset.append(i)
            backtrack(i + 1, subset, n, k)
            subset.pop()
            backtrack(i + 1, subset, n, k)
        
        backtrack(1, [], n, k)
        return res
