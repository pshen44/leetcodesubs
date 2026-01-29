class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProf = max(profit, maxProf)
            if prices[r] < prices[l]:
                l += 1
            else:
                r += 1
        return maxProf


