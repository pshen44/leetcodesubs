class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {')' : '(' , ']' : '[' , '}' : '{'}
        stack = []

        for bracket in s:
            if stack and bracket in ')]}':
                open = stack.pop()
                if bmap[bracket] != open:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False

