class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int begin = 0, end = nums.size() - 1;
        while (begin <= end){
            if (nums[begin] == val){
                nums[begin] = nums[end];
                end--;
            } else{
                begin++;
            }
        }
        return begin;
    }
};