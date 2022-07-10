class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int lenNums = nums.length-1, left = -1, right = -1, maxNums = nums[0], minNums = nums[nums.length - 1];
        for(int i=0; i<nums.length; i++){
            int a = nums[i], b = nums[lenNums - i];
            if(a < maxNums){
                right = i;
            } else{
                maxNums = a;
            }
            if(b > minNums){
                left = i;
            } else{
                minNums = b;
            }
        }
        return Math.max(0, left + right - lenNums + 1);
    }
}