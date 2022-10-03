class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int arithmeticSlices = 0, combination = 0, lastDifference = 0;
        for (int i=0; i<nums.length-1; i++){
            int difference = nums[i+1] - nums[i];
            if (i != 0 && difference == lastDifference){
                combination += 1;
                arithmeticSlices += combination;
            } else{
                combination = 0;
            }
            lastDifference = difference;
        }
        return arithmeticSlices;
    }
}