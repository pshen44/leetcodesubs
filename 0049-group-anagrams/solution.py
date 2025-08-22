class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordMap = defaultdict(list) # count : word
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            wordMap[tuple(count)].append(s)
        return list(wordMap.values())
