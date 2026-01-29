class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                res = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(int(res))
                continue
            if token == '*':
                res = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(int(res))
                continue
            if token == '/':
                res = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(res))
                continue
            if token == '-':
                res = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(res))
                continue
            stack.append(int(token))
        return stack[0]
