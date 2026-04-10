class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            if t in ['+','-','*','/']:
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '+':
                    result = left + right
                elif t == '-':
                    result = left - right
                elif t == '*':
                    result = left * right
                elif t == '/':
                    result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[-1]