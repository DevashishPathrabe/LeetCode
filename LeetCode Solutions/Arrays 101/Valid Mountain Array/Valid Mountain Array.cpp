class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if (A.size() < 3){
            return false;
        }
        int i = 1;
        while ((i < A.size()) && (A[i-1] < A[i])){
            i++;
        }
        if ((i == A.size()) || (i == 1)){
            return false;
        }
        while ((i < A.size()) && (A[i-1] > A[i])){
            i++;
        }
        return A.size() == i;
    }
};