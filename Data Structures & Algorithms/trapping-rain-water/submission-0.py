class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        # 從左往右掃，記錄到目前為止的最大值
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        # 從右往左掃
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        # 逐格算積水
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res