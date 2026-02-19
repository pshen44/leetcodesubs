class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while l <= r and r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] >= prices[l]:
                r += 1
            elif prices[r] < prices[l]:
                l += 1
        return res
