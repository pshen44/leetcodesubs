class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {} # num : idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sumMap:
                return [sumMap[diff], i]
            sumMap[n] = i

