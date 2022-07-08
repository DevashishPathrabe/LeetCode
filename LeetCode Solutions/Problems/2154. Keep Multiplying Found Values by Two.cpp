class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        sort(nums.begin(), nums.end());
        int result = 0;
        while (result == 0){
            result = 1;
            for (int i=0; i<nums.size(); i++){
                if (nums[i] == original){
                    original = nums[i];
                    original *= 2;
                    result = 0;
                }
            }   
        }
        return original;
    }
};