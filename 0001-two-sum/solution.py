class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in summap:
                return [i, summap[diff]]
            summap[n] = i
