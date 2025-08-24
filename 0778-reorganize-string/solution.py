class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        if max(freq) > (len(s) + 1) // 2:
            return ""
        res = []
        while len(res) < len(s):
            max_index = freq.index(max(freq))
            char = chr(max_index + ord('a'))
            res.append(char)
            freq[max_index] -= 1
            if freq[max_index] == 0:
                continue
            tmp = freq[max_index]
            freq[max_index] = float("-inf")
            nextMax_index = freq.index(max(freq))
            char = chr(nextMax_index + ord('a'))
            res.append(char)
            freq[max_index] = tmp
            freq[nextMax_index] -= 1
        return "".join(res)

