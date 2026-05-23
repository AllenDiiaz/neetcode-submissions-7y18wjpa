class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # piles = [1,4,3,2], h = 9
        # 一個 pile 能最快吃完的 r = 4 再快也不能吃到別的 pile
        # 最少都要 4 個 pile 時間
        # binary search 從裡面選 rate
        # 內部元素 // r 要無條件取下個整數 e.g. 1//4 -> 1 (而不是0)
        # 最後加總耗時跟 h 比較 超過 continue

        pile = len(piles) # 這樣知道最快要幾個時間
        # Binary search 左右指針
        left = 1     
        right = max(piles)
        # 建工具 
        import math

        # piles = [25,10,23,4], h = 4
        # 1 25 -> 13
        # 2 1 2 1 = 6
        # 13 25 -> 19
        # 2 1 2 1 = 6
        # 19 25 -> 22
        # 2 1 2 1 = 6
        # 22 25 -> 24
        # 2 1 1 1 = 5
        # 24 25 -> 25
        # 1 1 1 1 = 4

        ans = 0

        while left <= right:
            mid_r = (left+right) // 2
            total_cost = 0
            for p in piles:
                cost = math.ceil(p / mid_r)
                total_cost+= cost
            if total_cost > h:
                left = mid_r + 1
            else: # total_cost <= h
                ans = mid_r
                right = ans - 1

        return ans








        