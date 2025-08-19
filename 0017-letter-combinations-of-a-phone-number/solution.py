class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phonemap = {"2" : 'abc', "3" : 'def', "4" : 'ghi', "5" : 'jkl', "6" : 'mno', "7" : 'pqrs', "8" : 'tuv', "9" : 'wxyz'}
        res = []
        def backtrack(i, substring):
            if len(substring) == len(digits):
                res.append(substring)
                return
            for letter in phonemap[digits[i]]:
                backtrack(i + 1, substring + letter)

        backtrack(0, "")
        return res if res != [""] else []
