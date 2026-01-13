class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hmap:
                return [i,hmap[difference]]
            else:
                hmap[n] = i



