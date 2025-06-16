class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        array = list(range(len(nums) + 1))
        for i in array:
            if i not in nums:
                return i


