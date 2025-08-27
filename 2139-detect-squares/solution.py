from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            res += self.freq[(x, py)] * self.freq[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
