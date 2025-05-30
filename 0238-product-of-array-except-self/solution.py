class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = 1
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] *= pre
            pre *= nums[i]
        suf = 1
        for i in (range(len(nums) - 1, -1, -1)):
            result[i] *= suf
            suf *= nums[i]
        return result

