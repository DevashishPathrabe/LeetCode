class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = -1;
        int column = matrix[0].length;
        for(int i=0; i<matrix.length; i++){
            if(target <= matrix[i][column - 1]){
                row = i;
                break;
            }
        }
        if(row == -1){
            return false;
        }
        for(int k=0; k<matrix[0].length; k++){
            if(matrix[row][k] == target){
                return true;
            }
        }
        return false;
    }
}