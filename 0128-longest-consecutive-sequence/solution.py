class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                streak = 0
                while num + streak in numset:
                    streak += 1
                longest = max(longest, streak)
        return longest

                
