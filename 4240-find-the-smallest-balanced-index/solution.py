class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        pref = [1] * (len(nums) + 1)
        limit = sum(nums) + 1

        for i in range(len(nums) - 1, -1 , -1):
            prod = pref[i + 1] * nums[i]
            pref[i] = min(prod, limit)

        left = 0
        
        for i in range(len(nums)):
            
            if left == pref[i + 1]:
                return i
            left += nums[i]
            
        return -1
