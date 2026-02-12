class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {} # num : freq
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        # index is count, values are the values with that count
        for n in nums:
            freqmap[n] = 1 + freqmap.get(n, 0)
        
        for num, cnt in freqmap.items():
            freq[cnt].append(num)
        
        for j in range(len(freq) - 1, -1, -1):
            for num in freq[j]:
                res.append(num)
                if k == len(res):
                    return res
