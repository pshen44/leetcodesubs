class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        map = Counter(nums)
        freq_count = Counter(map.values())

        for n in nums:
            if freq_count[map[n]] == 1:
                return n

        return -1
