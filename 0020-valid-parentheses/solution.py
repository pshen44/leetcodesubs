class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bmap = { '}' : '{', ']' : '[', ')' : '(' }
        for b in s:
            if b in bmap:
                if stack and bmap[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
        


