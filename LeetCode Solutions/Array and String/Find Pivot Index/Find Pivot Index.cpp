class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if (nums.size() < 1){
            return -1;
        }
        int rightSum=0, leftSum=0;
        for (int i:nums){
            rightSum += i;
        }
        for (int i=0; i<nums.size(); i++){
            rightSum -= nums[i];
            if (rightSum == leftSum){
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};