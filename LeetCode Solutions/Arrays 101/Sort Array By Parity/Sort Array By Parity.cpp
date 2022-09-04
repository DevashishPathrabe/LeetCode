class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int left = 0, right = A.size() - 1, temp;
        while (left < right){
            if (A[left] % 2 == 1){
                temp = A[left];
                A[left] = A[right];
                A[right] = temp;
                right -= 1;
            } else{
                left += 1;
            }
        }
        return A;
    }
};