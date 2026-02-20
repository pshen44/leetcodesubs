class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        start = nums[0]
        b = float('inf') # smallest
        c = float('inf') # second smallest

        for n in nums[1:]:
            if n < b:
                c = b
                b = n
            elif n < c:
                c = n
        return start + b + c


