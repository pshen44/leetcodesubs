class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        strmap = set()
        
        for r in range(len(s)):
            while s[r] in strmap:
                strmap.remove(s[l])
                l += 1
            strmap.add(s[r])
            res = max(res, r - l + 1)
        return res

