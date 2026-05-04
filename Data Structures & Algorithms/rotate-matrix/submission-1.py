class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        n = len(matrix)
        # (0,0) (0,1) 
        # (1,0) (1,1) 
        # 1 2
        # 3 4

        # Transpose
        # 1 3
        # 2 4
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        # Reverse Rows
        # 3 1
        # 4 2
        for i in range(n):
            matrix[i].reverse()

        