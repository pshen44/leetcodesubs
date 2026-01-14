class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parMap = {')' : '(', ']' : '[', '}' : '{'}
        for n in range(len(s)):
            if s[n] in parMap:
                if stack and stack[-1] == parMap[s[n]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[n])
        return True if not stack else False

