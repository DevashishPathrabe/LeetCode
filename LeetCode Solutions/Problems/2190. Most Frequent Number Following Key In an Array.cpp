class Solution {
public:
    int mostFrequent(vector<int>& nums, int key) {
        int count[1001] = {}, result = 0;
        for (int i=1; i<nums.size(); ++i){
            if (nums[i - 1] == key && ++count[nums[i]] > count[result]){
                result = nums[i];
            }
        }
        return result;
    }
};