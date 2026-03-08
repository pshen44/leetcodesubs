class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:

        minIdx = -1
        prevCap = float("inf")
        
        for i, cap in enumerate(capacity):
            if itemSize <= cap:
                if cap < prevCap:
                    prevCap = cap
                    minIdx = i
        return minIdx
