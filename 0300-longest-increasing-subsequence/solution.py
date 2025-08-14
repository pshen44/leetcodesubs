class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)
        for i in range(len(nums) - 2, -1, -1):
            n = i
            while n < len(nums) - 1:
                if nums[i] < nums[n + 1]:
                    dp[i] = max(dp[i], 1 + dp[n + 1])
                n += 1
        return max(dp)
            
