class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 先得到有幾個col 因為那決定 // 跟 ％ 以誰來除
        col = len(matrix[0])
        # 要得知總共有幾個元素才知道 right指針
        row = len(matrix)
        element = row * col
        # 設定指針
        right = element - 1
        left = 0

        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] target = 15
        # 0 11 mid = 5 -> 1...1 -> 11
        # 6 11 mid = 8 -> 2...0 -> 14

        while left <= right:
            mid = (left + right) // 2
            loc_row = mid // col # 位在哪一個 row
            loc_col = mid % col  # 位在哪一個 col
            if matrix[loc_row][loc_col] == target:
                return True
            elif matrix[loc_row][loc_col] < target: # 往右找 left = mid + 1
                left = mid + 1
            elif matrix[loc_row][loc_col] > target: # 往右找 right = mid - 1
                right = mid - 1

        return False



 

        