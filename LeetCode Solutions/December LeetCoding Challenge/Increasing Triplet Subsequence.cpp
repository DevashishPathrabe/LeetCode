class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int left = INT_MAX, mid = INT_MAX;
        for(int i : nums){
            if(i <= left){
                left = i;
            }
            else if(i <= mid){
                mid = i;
            } else{
                return true;
            }
        }
        return false;
    }
};