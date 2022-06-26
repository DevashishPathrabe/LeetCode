class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        long long int p = pow(2, n);
        for (int i=0; i<p; i++){
            result.push_back(i^(i/2));
        }
        return result;
    }
};