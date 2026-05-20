class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # 建 stack 維護每根柱子能算的最大面積
        stack = [-1]
        # 面積的寬的算法是
        # (left + 1) - (right - 1) + 1
        # 因為left不能算 要向右遞移
        # right 不能算要向左遞移
        # 間隔是 後減前+1

        # 當前是
        # h  [7,1,7,2,2,4]
        # i   0 1 2 3 4 5
        # 為了方便計算
        # h    [7,1,7,2,2,4,0]
        # i -1  0 1 2 3 4 5 6
        heights.append(0)

        # 初始化最大面積 每次柱子的新面積都會跟之比較
        max_area = 0

        for idx, h in enumerate(heights):

            # 1. stack 有值 新柱子比等待柱子小 結算
            while stack and h < heights[stack[-1]]:
                wait_h_idx = stack.pop()
                curr_area = ( ((idx-1) - (stack[-1]+1)) + 1) * heights[wait_h_idx]
                max_area = max(curr_area,max_area)
            stack.append(idx)

        return max_area

        # stack [-1]
        # i = 0 h = 7
        # 3 -> stack[-1 0]

        # i = 1 h = 1
        # 1 -> stack [-1]
        # w_h  = pop 0
        # a = ((1-1) - (-1+1)) +1 * w_h = 7
        # push i = 1
        # stack [-1 1]

        # i = 2 h = 7
        # 2 -> stack [-1 1 2]

        # i = 3 h = 2
        # 1 -> stack [-1 1 2]
        # w_h = pop 2
        # a = ((3-1) - (1+1)) + 1 * w_h = 7
        # 




        
        