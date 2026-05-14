class Solution:
    def isValid(self, s: str) -> bool:

        # 括號要配對 建一個 dict
        # 括號配對要按照順序 先出現右括號 return Flase

        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for char in s:

            if char in mapping:
                top_element = stack.pop() if stack else "$"
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


        