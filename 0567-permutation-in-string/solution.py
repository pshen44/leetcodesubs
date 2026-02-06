class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = Counter(s1)
        count2 = {} # char : freq
        l = 0
        r = 0
        while r < len(s2):
            if (r - l + 1) > len(s1):
                #todo remove s2[l] from count2
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                l += 1
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if count1 == count2:
                return True
            r += 1
        return False

