class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countmap = {} # num : count
        length = len(nums)
        for n in nums:
            countmap[n] = 1 + countmap.get(n, 0)
        for num, count in countmap.items():
            if count >= (length / 2):
                return num
