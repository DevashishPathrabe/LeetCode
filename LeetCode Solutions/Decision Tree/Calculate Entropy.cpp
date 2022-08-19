class Solution {
public:
    double calculateEntropy(vector<int>& input) {
        unordered_map<int, int> umap;
        for(auto tmp: input) {
            umap[tmp]++;
        }
        double size = input.size(), result = 0, px;
        for(auto tmp: umap) {
            px = (tmp.second) / size;
            result -= px*log2(px);
        }
        return result;
    }
};