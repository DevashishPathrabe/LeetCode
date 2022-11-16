class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        for(int i=0, count=0; i<nums.size(); i++){
            if(nums[i] == 1 && count < k && i != 0){
                return false;
            }
            else if(nums[i] == 1){
                count = 0;
            } else{
                count++;
            }
        }
        return true;
    }
};