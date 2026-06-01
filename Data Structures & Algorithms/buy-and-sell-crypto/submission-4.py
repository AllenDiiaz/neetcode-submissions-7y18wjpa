class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 建 left right 指針
        # left 指針指最左邊
        # 開始往右掃
        # 如果 右掃遇到更低 則更新 left
        #     右掃遇到更高 則計算 profit 並跟 max_profit 比較

        # Input: prices = [10,1,5,6,7,1]

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            elif prices[right] > prices[left]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit,curr_profit)
            right+=1

        return max_profit

        
        