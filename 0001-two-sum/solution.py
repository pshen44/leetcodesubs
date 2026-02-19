class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in countmap:
                return [i, countmap[diff]]
            countmap[n] = i

