class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s

        tmap = Counter(t)
        window = {}
        have = 0
        need = len(tmap)
        res = [-1, -1]
        lenRes = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tmap and window[c] == tmap[c]:
                have += 1
            while have == need:
                if (r - l + 1) < lenRes:
                    res = [l, r]
                    lenRes = r - l + 1
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if lenRes != float("inf") else ""
            

