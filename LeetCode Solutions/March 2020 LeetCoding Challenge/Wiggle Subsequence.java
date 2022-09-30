class Solution {
    public int wiggleMaxLength(int[] nums) {
        int lenNums = nums.length, i = 1, length = 1;
        while(i < lenNums && nums[i] == nums[i-1]){
            i += 1;
        }
        if(i == lenNums){
            return 1;
        }
        boolean up = nums[i-1] > nums[i];
        while(i < lenNums){
            if((up && nums[i] < nums[i-1]) || (!up && nums[i] > nums[i-1])){
                up = !up;
                length += 1;
            }
            i += 1;
        }
        return length;
    }
}