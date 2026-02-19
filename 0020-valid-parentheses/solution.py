class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = { ')' : '(', '}' : '{', ']' : '[' }
        for p in s:
            if stack and p in pmap: # if stack and closing p
                if pmap[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False
