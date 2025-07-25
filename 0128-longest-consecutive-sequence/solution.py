class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = Counter(nums)
        for n in count:
            streak = 0
            if (n - 1) not in count:
                while n in count:
                    n += 1
                    streak += 1
            res = max(streak, res)
        return res

            



