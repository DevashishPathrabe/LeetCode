class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = -1;
        int column = matrix[0].size();
        for(int i=0; i<matrix.size(); i++){
            if(target <= matrix[i][column - 1]){
                row = i;
                break;
            }
        }
        if(row == -1){
            return false;
        }
        for(int k=0; k<matrix[0].size(); k++){
            if(matrix[row][k] == target){
                return true;
            }
        }
        return false;
    }
};