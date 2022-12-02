class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        int n = board.size();
        int rs = 0, cs = 0, rm = 0, cm = 0;
        for (int i=0; i<n; i++){
            bool rf = board[0][0] == board[i][0], cf = board[0][0] == board[0][i];
            rs += rf, cs += cf;
            rm += rf ^ !(i & 1), cm += cf ^ !(i & 1);
            for (int j=0; j<n; j++){
                if ((board[0][j] == board[i][j]) ^ rf || (board[j][0] == board[j][i]) ^ cf){
                    return -1;
                }
            }
        }
        if (n % 2 == 0){
            if (rs == n / 2 && cs == n / 2){
                return min(rm, n - rm) / 2 + min(cm, n - cm) / 2;
            }
            return -1;
        }
        int result = 0;
        if (rs == n / 2){
            result += (n - rm) / 2;
        }
        else if (rs == n / 2 + 1){
            result += rm / 2;
        }
        else{
            return -1;
        }
        if (cs == n / 2){
            result += (n - cm) / 2;
        }
        else if (cs == n / 2 + 1){
            result += cm / 2;
        }
        else{
            return -1;
        }
        return result;
    }
};