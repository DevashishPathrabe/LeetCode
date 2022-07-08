class Solution {
    public int findFinalValue(int[] nums, int original) {
        Arrays.sort(nums);
        int result = 0;
        while (result == 0){
            result = 1;
            for (int i=0; i<nums.length; i++){
                if (nums[i] == original){
                    original = nums[i];
                    original *= 2;
                    result = 0;
                }
            }   
        }
        return original;
    }
}