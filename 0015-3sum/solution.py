class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()

        for i, target in enumerate(nums):
            if i > 0 and nums[i - 1] == target:
                continue

            l = i + 1
            r = len(nums) - 1

            while r > l:
                tsum = nums[l] + nums[r] + target
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
        return res
