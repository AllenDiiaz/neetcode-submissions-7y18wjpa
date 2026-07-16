class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        num_ele = row * col

        left = 0
        right = num_ele - 1

        while left <= right:

            mid  = left + (right-left) // 2

            loc_row = mid // col
            loc_rol = mid % col

            if (matrix[loc_row][loc_rol] == target):
                return True

            elif (matrix[loc_row][loc_rol] > target):
                right = mid - 1

            elif (matrix[loc_row][loc_rol] < target):
                left = mid + 1

        return False




         