class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}
        count2 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        l, r = 0, 0
        while r - l + 1 < len(s1):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            r += 1
        while r < len(s2):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if count2 == count1:
                return True
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            r += 1
        return False


        
        
