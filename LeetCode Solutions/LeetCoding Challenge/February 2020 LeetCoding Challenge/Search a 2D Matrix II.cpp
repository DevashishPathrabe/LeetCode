class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0, column = matrix[0].size() - 1;
        while(row < matrix.size() && column >= 0){
            if(matrix[row][column] > target){
                column--;
            }
            else if(matrix[row][column] < target){
                row++;
            } else{
                return true;
            }
        }
        return false;
    }
};