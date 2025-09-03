from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for x, y in points:
            orig_dist = (((0 - x) ** 2) + (0 - y) ** 2) ** (1 / 2)
            dist.append([orig_dist, x, y])

        heapq.heapify(dist)

        while k > 0:
            trp = heapq.heappop(dist)
            res.append([trp[1], trp[2]])
            k -= 1
        return res


        


