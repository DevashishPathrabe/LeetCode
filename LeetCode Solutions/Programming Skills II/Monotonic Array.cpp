class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increasing = false, decreasing = false;
        for (int i=0; i<nums.size()-1; i++){
            if (nums[i+1] > nums[i]){
                increasing = true;
            }
            if (nums[i+1] < nums[i]){
                decreasing = true;
            }
            if (increasing == true && decreasing == true){
                return false;
            }
        }
        return true;
    }
};