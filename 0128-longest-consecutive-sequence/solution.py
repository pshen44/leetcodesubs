class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        maxS = 0
        if nums == []:
            return 0
        for num in count:
            streak = 1
            if (num - 1) not in count: # is num start of a sequence
                while (num + streak) in count: # while the next i number(s) are in count
                    streak += 1
            maxS = max(streak, maxS)
        return (maxS)

            
            

            
