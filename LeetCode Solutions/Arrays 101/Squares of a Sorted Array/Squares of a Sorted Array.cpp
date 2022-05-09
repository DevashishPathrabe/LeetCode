class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for (int& number : A){
            number *= number;
        }
        sort(A.begin(), A.end());
        return A;
    }
};