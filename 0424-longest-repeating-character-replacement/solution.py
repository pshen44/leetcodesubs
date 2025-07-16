class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLen = 0
        mostfreq = 0
        strMap = defaultdict()
        for r in range(len(s)):
            strMap[s[r]] = 1 + strMap.get(s[r], 0)
            mostfreq = max(mostfreq, strMap[s[r]])
            while (r - l + 1) - mostfreq > k:
            # streak broken
                strMap[s[l]] -= 1
                l += 1
            maxLen = max(r - l + 1, maxLen)
        return maxLen




