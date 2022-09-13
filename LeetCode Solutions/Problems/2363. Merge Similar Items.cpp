class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int,int> m;
        for (auto v : items1){
            m[v[0]] += v[1];
        }
        for (auto v : items2){
            m[v[0]] += v[1];
        }
        items1.clear();
        for (auto v : m){
            items1.push_back({v.first, v.second});
        }
        return items1;
    }
};