class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        map = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []



        
