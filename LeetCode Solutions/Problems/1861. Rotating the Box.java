class Solution {
    public char[][] rotateTheBox(char[][] box) {
        int row = box.length, col =  box[0].length;
        char[][] result = new char[col][row];
        for(int i=0;i<row;i++){
            for(int j=col-2; j>=0; j--){
                if(box[i][j] == '#'){
                    int finalIndex = j + 1;
                    while(finalIndex < col && box[i][finalIndex] == '.'){
                         finalIndex++;
                    }
                    if (box[i][finalIndex - 1] == '.') {
                        char temp = box[i][finalIndex - 1];
                        box[i][finalIndex - 1] = box[i][j];
                        box[i][j] = temp;
                    }
                }
            }
        }
        for(int i=0;i<row;i++){
            for(int j=0; j<col; j++){
                result[j][i] = box[row-1-i][j];
            }
        }
        return result;
    }
}