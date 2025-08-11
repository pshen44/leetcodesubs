class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in count:
                return [count[diff], i]
            count[v] = i
