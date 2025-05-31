class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in (range(len(nums) - 1, -1, -1)):
            result[i] *= suffix
            suffix *= nums[i]
        return result

