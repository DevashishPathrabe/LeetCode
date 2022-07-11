class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int length = nums.length;
        int min, max;
        min = max = nums[0];
        for (int i=1; i<length; i++){
            if (nums[i] > max){
                max = nums[i];
            }
            else if (nums[i] < min){
                min = nums[i];
            }
        }
        min += Math.min(max - min, k);
        max -= Math.min(max - min, k);
        return max - min;
    }
}