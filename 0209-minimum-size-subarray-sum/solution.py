class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        minLen = float('inf')
        while r < len(nums):
            total += nums[r]
            while total >= target:
                minLen = min((r - l + 1), minLen)
                total -= nums[l]
                l += 1
            r += 1
            print(total)
        return 0 if minLen == float('inf') else minLen
