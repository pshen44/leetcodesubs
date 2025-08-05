class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #pick nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            #don't pick nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return res
