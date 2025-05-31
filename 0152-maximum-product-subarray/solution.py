class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        arraymax, arraymin = 1, 1
        for i in nums:
            temp = i * arraymax
            arraymax = max(i * arraymax, i * arraymin, i)
            arraymin = min(temp, i * arraymin, i)
            result = max(result, arraymax)
        return result
