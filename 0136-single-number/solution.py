class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countmap = {}
        for num in nums:
            countmap[num] = 1 + countmap.get(num, 0)
        return min(countmap, key = countmap.get)
        

