class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert] = nums[i]
                if i != insert:
                    nums[i] = 0
                insert += 1
