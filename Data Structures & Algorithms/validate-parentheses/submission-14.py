class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for char in s:

            if char in mapping:
                top_ele = stack.pop() if stack else "%"

                if top_ele != mapping[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0
        