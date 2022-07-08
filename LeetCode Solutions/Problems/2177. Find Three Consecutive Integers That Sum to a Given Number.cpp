class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        vector <long long> result;
        if ((num%3)!= 0){
            return result;
        }
        long long n = num/3;
        for (long long i=n-1; i<=n+1; i++){
            result.push_back(i);
        }
        return result;
    }
};