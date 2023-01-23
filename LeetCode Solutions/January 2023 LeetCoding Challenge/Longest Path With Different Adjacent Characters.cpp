class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int n = s.size(), result = 0;
        vector<vector<int>> children(n, vector<int>());
        for (int i=1; i<n; ++i){
            children[parent[i]].push_back(i);
        }
        helper(children, s, result, 0);
        return result;
    }

    int helper(vector<vector<int>>& children, string& s, int& result, int i) {
        int big1 = 0, big2 = 0;
        for (int& j : children[i]){
            int current = helper(children, s, result, j);
            if (s[i] == s[j]){
                continue;
            }
            if (current > big2){
                big2 = current;
            }
            if (big2 > big1){
                swap(big1, big2);
            }
        }
        result = max(result, big1 + big2 + 1);
        return big1 + 1;
    }
};