class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        waiting_day = []
        n = len(temperatures)
        result = [0] * n

        # temperatures = [30,38,30,36,35,40,28]

        for curr_idx in range(n):

            curr_temp = temperatures[curr_idx]

            while len(waiting_day) > 0 and curr_temp > temperatures[waiting_day[-1]]:

                prev_idx = waiting_day.pop()
                waited = curr_idx - prev_idx
                result[prev_idx] = waited

            waiting_day.append(curr_idx)

        return result





        

        