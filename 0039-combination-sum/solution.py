class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        def backtrack(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return
            if sum(subset) > target or i >= len(candidates): #or (sum(subset) + candidates[i]) > target:
                return
            
            #pick same number
            subset.append(candidates[i])
            backtrack(i)
            subset.pop()

            #pick candidates[i + 1]
            subset.append(candidates[i])
            backtrack(i + 1)

            #don't pick
            subset.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return res


