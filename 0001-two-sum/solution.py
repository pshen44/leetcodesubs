class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {} #number : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nummap:
                return [i, nummap[diff]]
            nummap[n] = i
