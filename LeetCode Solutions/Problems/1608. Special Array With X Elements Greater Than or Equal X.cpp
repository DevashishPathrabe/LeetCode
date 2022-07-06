class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i=1; i<=nums.size(); ++i){
            if(nums.size() - (lower_bound(nums.begin(), nums.end(), i) - nums.begin()) == i){
                return i;
            }
        }
        return -1;
    }
};