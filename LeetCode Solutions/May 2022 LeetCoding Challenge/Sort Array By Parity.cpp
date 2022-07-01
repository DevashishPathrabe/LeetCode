class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int left = 0, right = nums.size() - 1, temp;
        while(left < right){
            if(nums[left] % 2 == 1){
                temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                right -= 1;
            } else{
                left += 1;
            }
        }
        return nums;
    }
};