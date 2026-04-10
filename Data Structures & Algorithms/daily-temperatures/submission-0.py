class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)
        result = [0] * n

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                result[prev] = idx - prev
            stack.append(idx)

        return result