class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        hmap = Counter(bulbs)
        res = []

        for bulb, freq in hmap.items():
            if freq % 2 != 0:
                res.append(bulb)
        return sorted(res)
                
