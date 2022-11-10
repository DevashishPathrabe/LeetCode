class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for (int i=0, j=0; i<size(nums); ++i){
            if (i+1 < size(nums) and nums[i] == nums[i + 1]){
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
            if (nums[i]){
                swap(nums[j++], nums[i]);
            }
        }   
        return nums;
    }
};