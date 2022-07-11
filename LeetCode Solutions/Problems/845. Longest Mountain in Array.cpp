class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int left = 0;
        int right = 1;
        int length = 0;
        while(right < arr.size()){
            if(arr[left] >= arr[right]){
                left += 1;
                right += 1;
            } else{
                int haveRight = 0;
                while(right < (arr.size()-1) && arr[right] < arr[right+1]){
                    right += 1;
                }
                while(right < (arr.size()-1) && arr[right] > arr[right+1]){
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