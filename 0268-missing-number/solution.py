class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_sum = sum(list(range(len(nums)+1)))
        return array_sum - sum(nums)
        
