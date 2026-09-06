class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)
        pairs = 0
        for w in words:
            key = ''.join(sorted(set(w)))
            pairs += freq[key]
            freq[key] += 1
        return pairs
            
