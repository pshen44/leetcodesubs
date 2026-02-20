class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i, n = 0, len(s)
        res = []

        if len(s) == 1:
            return 0
        while i < n:
            cnt = 1
            while i + 1 < n and s[i + 1] == s[i]:
                cnt += 1
                i += 1
            res.append(cnt)
            i += 1
        ans = 0
        for i in range(1, len(res)):
            ans += min(res[i - 1], res[i])
        return ans
        

