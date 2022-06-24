class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> m(60, 0);
        int result = 0;
        for (auto t: time){
            result += m[(60 - t % 60) % 60];
            m[t % 60] += 1;
        }
        return result;
    }
};