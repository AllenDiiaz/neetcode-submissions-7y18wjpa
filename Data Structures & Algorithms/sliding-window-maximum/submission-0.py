from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()          # 存 index，對應的值由大到小
        res = []
        left = 0

        for right in range(len(nums)):
            # ② 丟掉隊尾所有比新元素小的（它們永遠贏不了）
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            # ① 隊首已經滑出視窗了就丟掉
            if dq[0] < left:
                dq.popleft()

            # 視窗滿了才開始記錄答案
            if right + 1 >= k:
                res.append(nums[dq[0]])
                left += 1

        return res