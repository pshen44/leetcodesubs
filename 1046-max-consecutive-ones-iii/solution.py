class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        zcount = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zcount += 1
            while zcount > k:
                if nums[l] == 0:
                    zcount -= 1
                l += 1
            maxLen = max(maxLen, (r - l + 1))
        return maxLen
                
