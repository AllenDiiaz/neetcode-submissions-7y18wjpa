class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        stack = [-1]
        max_area = 0

        for idx,ht in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > ht:
                mid = stack.pop()
                curr_ht = heights[mid]
                width = idx - stack[-1] - 1 
                max_area = max(max_area, width * curr_ht)

            stack.append(idx)

        return max_area





        