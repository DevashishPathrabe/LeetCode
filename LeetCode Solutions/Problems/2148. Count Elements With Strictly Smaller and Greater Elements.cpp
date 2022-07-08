class Solution {
public:
    int countElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int minimum = nums[0];
        int maximum = nums[nums.size() - 1];
        int count = 0;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] > minimum && nums[i] < maximum){
                count += 1;
            }
        }
        return count;
    }
};