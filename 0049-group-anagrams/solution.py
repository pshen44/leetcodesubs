class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list) # word : freqmap
        for s in strs:
            freqmap = [0] * 26
            for c in s:
                freqmap[ord('a') - ord(c)] += 1
            hmap[tuple(freqmap)].append(s)
        return list(hmap.values())
