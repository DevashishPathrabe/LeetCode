class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int ans = 1;
        sort(nums.begin(), nums.end());
        long sums = 0;
        for(int r, l = 0; r < nums.size(); r++){
            sums += nums[r];
            while(l < r && sums + k < long(nums[r]) * (r - l + 1))  sums -= nums[l++];
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};