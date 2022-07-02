class Solution {
public:
    int longestMountain(vector<int>& A) {
        int left = 0;
        int right = 1;
        int length = 0;
        while(right < A.size()){
            if(A[left] >= A[right]){
                left += 1;
                right += 1;
            } else{
                int haveRight = 0;
                while(right < (A.size()-1) && A[right] < A[right+1]){
                    right += 1;
                }
                while(right < (A.size()-1) && A[right] > A[right+1]){
                    right += 1;
                    haveRight = 1;
                }
                if(haveRight != 0){
                    length = max(length,right-left+1);
                }
                left = right;
                right = left + 1;
            }
        }
        return length;
    }
};