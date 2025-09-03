class TimeMap:

    def __init__(self):
        self.timemap = {} #key : [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timemap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp > self.timemap[key][mid][1]:
                l = mid + 1
                res = self.timemap[key][mid][0]
            elif timestamp < self.timemap[key][mid][1]:
                r = mid - 1
            elif timestamp == self.timemap[key][mid][1]:
                return self.timemap[key][mid][0]
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
