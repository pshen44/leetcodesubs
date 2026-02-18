class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [-1] * len(nums)

        def dfs(i, end):
            if i >= end:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1, end), dfs(i + 2, end) + nums[i])
            return memo[i]

        res1 = dfs(1, len(nums))

        memo = [-1] * len(nums)
        res2 = dfs(0, len(nums) - 1)
        return max(res1, res2)


