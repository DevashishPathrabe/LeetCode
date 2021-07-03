class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result (n, vector<int>(n));
        int count = 1;
        for(int layer=0; layer<(n + 1)/2; layer++){
            for(int ptr=layer; ptr<n-layer; ptr++){
                result[layer][ptr] = count++;
            }
            for(int ptr=layer+1; ptr<n-layer; ptr++){
                result[ptr][n - layer - 1] = count++;
            }
            for(int ptr=n-layer-2; ptr>=layer; ptr--){
                result[n-layer-1][ptr] = count++;
            }
            for(int ptr=n-layer-2; ptr>layer; ptr--){
                result[ptr][layer] = count++;
            }
        }
        return result;
    }
};