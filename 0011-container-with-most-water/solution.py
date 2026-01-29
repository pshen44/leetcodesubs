class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            area = min(height[l], height[r]) * width
            maxA = max(maxA, area)
            if height[l] > height[r]:
                r -= 1
            elif height[r] >= height[l]:
                l += 1
        return maxA



