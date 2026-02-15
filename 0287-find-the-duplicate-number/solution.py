class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nummap = Counter(nums)
        for num, cnt in nummap.items():
            if cnt >= 2:
                return num
