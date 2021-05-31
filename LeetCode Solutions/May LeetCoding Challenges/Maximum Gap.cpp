class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if(nums.size() <= 1){
            return 0;
        }
        sort(nums.begin(), nums.end());
        int maximumDifference = 0;
        for(int num=1; num<nums.size(); num++){
            maximumDifference = max(maximumDifference, nums[num]-nums[num - 1]);
        }
        return maximumDifference;
    }
};