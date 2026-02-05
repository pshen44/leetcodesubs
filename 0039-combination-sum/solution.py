class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or sum(subset) > target:
                return
            subset.append(candidates[i])
            backtrack(i)
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res
