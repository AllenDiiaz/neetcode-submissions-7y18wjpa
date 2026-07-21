class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int row = matrix.size();
        int col = matrix[0].size();
        int ele = row * col;
        int left = 0;
        int right = ele - 1;

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
