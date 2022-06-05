class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int lenNums = nums.size()-1, left = -1, right = -1, maxNums = nums[0], minNums = nums[nums.size() - 1];
        for (int i=0; i<nums.size(); i++){
            int a = nums[i], b = nums[lenNums - i];
            if (a < maxNums){
                right = i;
            } else{
                maxNums = a;
            }
            if (b > minNums){
                left = i;
            } else{
                minNums = b;
            }
        }
        return max(0, left + right - lenNums + 1);
    }
};