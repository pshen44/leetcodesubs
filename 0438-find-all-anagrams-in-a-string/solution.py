class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l, r = 0, 0
        sCount = {} # str : int
        pCount = {} # str : int
        for c in p:
            pCount[c] = 1 + pCount.get(c, 0)
        res = []
        while r - l + 1 <= len(p):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            r += 1
        
        while r < len(s):
            if sCount == pCount:
                res.append(l)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                del sCount[s[l]]
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            l += 1
            r += 1
        if sCount == pCount:
            res.append(l)


        return res
                
            
