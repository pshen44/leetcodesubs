class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(array):
            rob1, rob2 = 0, 0
            for n in array:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(helper(nums[0:len(nums) - 1]), helper(nums[1:len(nums)])) if len(nums) > 1 else nums[0]
