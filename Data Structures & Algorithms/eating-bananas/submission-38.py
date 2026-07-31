class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # piles = [1,4,3,2], h = 9
        left = 1
        right = max(piles)

        ans = right

        while left <= right:

            mid = left + (right-left) // 2

            total_cost_h = 0

            for banana in piles:
                total_cost_h += math.ceil(banana / mid)

            if total_cost_h > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans
        