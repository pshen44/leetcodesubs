class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #if open < n add open
        #if closed < open add closed
        #all equal = done
        stack = []
        res = []
        def backtrack(closedN, openN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(closedN, openN + 1)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(closedN + 1, openN)
                stack.pop()
            
        backtrack(0, 0)
        return res

