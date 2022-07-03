class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int a = values[0], b = 0;
        for (int i=1; i<values.size(); i++){
            b = max(a + values[i] - i, b);
            a = max(values[i] + i, a);
        }
        return b;
    }
};