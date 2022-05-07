class Solution {
    public int removeElement(int[] nums, int val) {
        int begin = 0, end = nums.length - 1;
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
}