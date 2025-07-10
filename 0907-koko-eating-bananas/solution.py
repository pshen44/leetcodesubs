class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            i = 0
            m = (l + r) // 2
            for pile in piles:
                i += math.ceil(pile / m)

            if i <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
