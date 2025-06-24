class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        orig = nums
        for i in range(len(orig)):
            nums.append(nums[i])
        return nums
