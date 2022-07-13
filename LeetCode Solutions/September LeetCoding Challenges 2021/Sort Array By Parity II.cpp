class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int i = 0, j = 1;
        while (i < nums.size() and j < nums.size()-1 || i < nums.size()-1 and j < nums.size()){
            if (nums[i]%2 == 0 and nums[j]%2 == 1){
                i += 2;
                j += 2;
            }
            else if (nums[i]%2 == 1 and nums[j]%2 == 0){
                swap(nums[i],nums[j]);
                i += 2;
                j += 2;
            }
            else if (nums[i]%2 == 0 and nums[j]%2 == 0){
                i += 2;
            } else{
                j += 2;
            }
        }
        return nums;
    }
};