class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_prices = float('Inf')
        max_profit = 0

        for price in prices:
            if price < min_prices:
                min_prices = price

            elif price - min_prices > max_profit:
                max_profit = price - min_prices

        return max_profit

        