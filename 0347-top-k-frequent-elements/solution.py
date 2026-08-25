class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        freqs = [[] for i in range(len(nums) + 1)] #index is count, value is nums with that count
        res = []

        for n in nums:
            fmap[n] = 1 + fmap.get(n, 0)

        for value, count in fmap.items():
            freqs[count].append(value)

        for i in range(len(freqs) -1, -1, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res

