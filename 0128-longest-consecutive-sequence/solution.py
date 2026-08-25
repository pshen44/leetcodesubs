class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        res = 0
        # we want to keep the current streak in a set containing all current nums in a streak

        for n in pool:
            if (n - 1) not in pool:
                streak = 1
                while n + streak in pool:
                    streak += 1
                res = max(res, streak)
        return res


