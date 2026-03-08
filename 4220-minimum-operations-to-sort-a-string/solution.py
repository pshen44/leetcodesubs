class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0


        t = ''.join(sorted(s))

        if s == t:
            return 0
        if len(s) == 2:
            return -1
        l, r = 0, len(s) - 1
        while l < len(s) and s[l] == t[l]:
            l += 1
        while r >= 0 and s[r] == t[r]:
            r -= 1
            
        if l > 0 or r < len(s) - 1:
            return 1

        mx = max(s)
        mn = min(s)

        if mx == s[0] and s.count(mx) == 1 and mn == s[-1] and s.count(mn) == 1:
            return 3
        return 2
