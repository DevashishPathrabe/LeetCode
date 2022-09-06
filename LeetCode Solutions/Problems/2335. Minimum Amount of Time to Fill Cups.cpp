class Solution {
public:
    int fillCups(vector<int>& amount) {
        int maximum = 0, sum = 0;
        for(int& a: amount) {
            maximum = max(a, maximum);
            sum += a;
        }
        return max(maximum, (sum + 1) / 2);
    }
};