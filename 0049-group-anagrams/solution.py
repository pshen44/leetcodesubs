class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap = defaultdict(list) # [count] : str
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord('a') - ord(c)] += 1
            anamap[tuple(count)].append(w)
        return list(anamap.values())
