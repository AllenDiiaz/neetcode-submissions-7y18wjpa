class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        # tokens = ["1","2","+","3","*","4","-"]

        # 1: [1]
        # 2: [1,2]
        # 3: right=2 left=1 result = left + right = 3 [3]
        # 4: [3,3]
        # 5: right=3 left=3 result = left * right = 9 [9]
        # 6: [9,4]
        # 7: right = 4 left=9 result = left-right= 5 [5]
        # return stack[-1] = 5

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

        return stack[0]