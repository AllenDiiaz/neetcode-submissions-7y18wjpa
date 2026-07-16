class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        // matrix = [[1,2,4,8],
        //           [10,11,12,13],
        //           [14,20,30,40]], target = 10

        int row = matrix.size();
        int col = matrix[0].size();
        int num_ele = row * col;

        int left = 0;
        int right = num_ele - 1;

        while (left<=right)
        {
            int mid = left + (right-left) / 2;
            int loc_row = mid / col;
            int loc_col = mid % col;

            if (matrix[loc_row][loc_col] == target) return true;

            else if (matrix[loc_row][loc_col] > target) right = mid - 1;

            else if (matrix[loc_row][loc_col] < target) left = mid + 1;
        }

        return false;
        
    }
};
