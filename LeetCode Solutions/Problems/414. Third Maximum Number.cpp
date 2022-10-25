class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i=1;
        for (int j=1; j<nums.size(); j++) 
            if (nums[j] != nums[j-1]) 
                nums[i++] = nums[j];
        if (i < 3){
            return nums[i-1];
        }
        return nums[i-3];
    }
};