class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if t == '*':
                    stack.append(op1 * op2)
                if t == '+':
                    stack.append(op1 + op2)
                if t == '/':
                    stack.append(op2 / op1)
                if t == '-':
                    stack.append(op2 - op1)
            else:
                stack.append(t)

        return int(stack.pop())

