class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        pairs = self.timemap.get(key, [])
        l, r = 0, len(pairs) - 1
        if key in self.timemap:
            while l <= r:
                mid = (l + r) // 2
                if pairs[mid][1] <= timestamp:
                    l = mid + 1
                    res = (pairs[mid][0])
                else:
                    r = mid - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
