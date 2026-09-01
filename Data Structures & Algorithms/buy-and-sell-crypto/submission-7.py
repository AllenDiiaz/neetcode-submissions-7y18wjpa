class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # prices = [10,1,5,6,7,1]

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):

            if prices[right] < prices[left]:
                left = right
            elif prices[right] > prices[left]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(curr_profit, max_profit)
            else:
                pass
            right+= 1

        return max_profit

        