class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                for j in range(i - 1, start - 1, -1):
                    res += s[j]
                if i != len(s):
                    res += " "
                start = i + 1
        return res
