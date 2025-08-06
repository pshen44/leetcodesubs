class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            if i > n:
                if len(subset) == k:
                    res.append(subset.copy())
                return
            
            subset.append(i)
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return res
        
