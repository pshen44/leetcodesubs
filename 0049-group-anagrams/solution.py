class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            scount = [0] * 26
            for char in s:
                scount[ord('a') - ord(char)] += 1
            hmap[tuple(scount)].append(s)
        return list(hmap.values())
