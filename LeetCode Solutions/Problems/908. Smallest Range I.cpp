class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int length = nums.size();
        int minimum, maximum;
        minimum = maximum = nums[0];
        for (int i=1; i<length; i++){
            if (nums[i] > maximum){
                maximum = nums[i];
            }
            else if (nums[i] < minimum){
                minimum = nums[i];
            }
        }
        minimum += min(maximum - minimum, k);
        maximum -= min(maximum - minimum, k);
        return maximum - minimum;
    }
};