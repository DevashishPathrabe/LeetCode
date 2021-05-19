class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int minimumNumberOfMoves = 0, median = median = nums[~~(nums.size() / 2)];
        for(int num : nums){
            minimumNumberOfMoves += abs(median - num);
        }
        return minimumNumberOfMoves;
    }
};