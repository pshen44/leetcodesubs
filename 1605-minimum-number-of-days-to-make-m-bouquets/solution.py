class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def validDay(days):
            streak = 0
            bouq = 0
            for f in bloomDay:
                if f <= days:
                    streak += 1
                    if streak == k:
                        bouq += 1
                        streak = 0
                else:
                    streak = 0
            return bouq >= m
    
        l, r = 1, max(bloomDay)

        while l < r:
            mid = (l + r) // 2
            if validDay(mid):
                r = mid
            else:
                l = mid + 1
        return l
                
