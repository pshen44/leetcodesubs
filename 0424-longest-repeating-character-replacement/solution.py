class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxLength = 0
        mostFreq = 0
        strmap = defaultdict()
        while r < len(s):
            strmap[s[r]] = 1 + strmap.get(s[r], 0)
            mostFreq = max(mostFreq, strmap[s[r]])
            while (r - l + 1) - mostFreq > k:
                strmap[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength
                
        
