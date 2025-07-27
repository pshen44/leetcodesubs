class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            maxP = max(profit, maxP)
            r += 1
        return maxP

