class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        substring = []
        for r in range(len(s)):
            while s[r] in substring:
                substring.pop(0)
                l += 1
            maxLen = max((r - l) + 1, maxLen)
            substring.append(s[r])
            print(maxLen)
            print(substring)
        return maxLen
