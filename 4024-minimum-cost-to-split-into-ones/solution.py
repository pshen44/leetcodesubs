class Solution:
    def minCost(self, n: int) -> int:
        
        memo = {}

        def backtrack(x):
            if x == 1:
                return 0
            if x in memo:
                return memo[x]
            mini = float("inf")

            for a in range(1,x):
                b = x - a
                curr = a * b
                total = curr + backtrack(a) + backtrack(b)
                mini = min(mini, total)
                
            memo[x] = mini
                
            return mini
        return backtrack(n)
