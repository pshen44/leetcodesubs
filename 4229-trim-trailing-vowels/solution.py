class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        tc = 0
        for c in s:
            if c in "aeiou":
                tc += 1
            else:
                tc = 0
        return s[0:-tc] if tc > 0 else s
