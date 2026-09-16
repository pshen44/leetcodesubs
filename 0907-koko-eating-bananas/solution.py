class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2
            hours = 0
            #try m as k
            for p in piles:
                hours += ceil(p / m)
            if hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
            

