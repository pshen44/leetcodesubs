class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opened, closed, path):
            if opened < n:
                backtrack(opened + 1, closed, path + '(')
            if closed < opened:
                backtrack(opened, closed + 1, path + ')')
            if closed == n and opened == n:
                res.append(path)
                return
        backtrack(0, 0, "")
        return res
