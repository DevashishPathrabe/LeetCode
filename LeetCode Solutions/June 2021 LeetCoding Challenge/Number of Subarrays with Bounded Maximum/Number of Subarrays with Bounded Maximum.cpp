class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int numberOfSubarrays = 0, lower = 0, middle = 0;
        for (int num:nums){
            if (num > right){
                middle = 0;
            } else{
                numberOfSubarrays += ++middle;
            }
            if (num >= left){
                lower = 0;
            } else{
                numberOfSubarrays -= ++lower;
            }
        }
        return numberOfSubarrays;
    }
};