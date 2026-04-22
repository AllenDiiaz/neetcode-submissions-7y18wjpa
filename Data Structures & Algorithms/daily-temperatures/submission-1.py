class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)
        result = [0] * n

        # temperatures = [30,38,30,36,35,40,28]
        # 0 30
        # stack = [] -> stack = [0]
        # 1 38
        # 

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                result[prev] = idx - prev
            stack.append(idx)

        return result