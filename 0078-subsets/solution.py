class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            # pick nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            
            #don't pick
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
