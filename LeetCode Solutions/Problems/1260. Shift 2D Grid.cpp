class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> result(m, vector<int>(n, 0));
        for (int i=0; i<n*m; i++){
           int temp =(i+k) % (n*m);
           result[temp/n][temp%n] = grid[i/n][i%n];
        }
        return result;
    }
};