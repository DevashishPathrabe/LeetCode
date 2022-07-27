class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean increasing = false, decreasing = false;
        for (int i=0; i<nums.length-1; i++){
            if (nums[i+1] > nums[i]){
                increasing = true;
            }
            if (nums[i+1] < nums[i]){
                decreasing = true;
            }
            if (increasing == true && decreasing == true){
                return false;
            }
        }
        return true;
    }
}