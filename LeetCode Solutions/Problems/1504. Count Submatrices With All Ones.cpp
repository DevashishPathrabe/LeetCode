class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int i, j, r = mat.size(), c = mat[0].size();
        int dpc[r][c];
        memset(dpc, 0, sizeof(dpc));
        for (i=0; i<r; i++){
            for (j=0; j<c; j++){
                if (i == 0){
                    if (mat[i][j]){
                        dpc[i][j] = 1;
                    }
                }
                else{
                    if (mat[i][j]){
                        dpc[i][j] = 1 + dpc[i-1][j];
                    }
                }
            }
        }
        int ans = 0;
        for (i=0; i<r; i++){
            for (j=0; j<c; j++){
                if (mat[i][j]){
                    int mn = dpc[i][j];
                    for (int k=j; k>=0; k--){
                        if (dpc[i][k]){
                            mn = min(dpc[i][k], mn);
                            ans += mn;
                        }
                        else
                            break;
                    }
                }
            }
        }
        return ans;
    }
};