class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                r = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(int(r))
                continue
            if tokens[i] == '-':
                r = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(r))
                continue
            if tokens[i] == '*':
                r = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(int(r))
                continue
            if tokens[i] == '/':
                r = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(r))
                continue
            stack.append(int(tokens[i]))
        return stack[0]

