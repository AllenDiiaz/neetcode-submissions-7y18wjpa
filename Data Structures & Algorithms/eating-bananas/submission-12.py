class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # piles = [1,4,3,2], h = 9
        # fetch min and max rate
        # using binary search to find best rate
        
        left = 1
        right = max(piles)

        import math

        ans = 0

        while left <= right:
            mid_r = (left+right) // 2
            total_cost = 0
            for p in piles:
                cost = math.ceil(p / mid_r)
                total_cost += cost
            if total_cost > h:
                left = mid_r + 1
            else:
                ans = mid_r
                right = mid_r - 1

        return ans 


        