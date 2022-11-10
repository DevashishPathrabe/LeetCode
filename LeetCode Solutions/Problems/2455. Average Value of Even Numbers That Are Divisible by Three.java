class Solution {
    public int averageValue(int[] nums) {
        int result = 0, count = 0;
        for (int i=0; i<nums.length; i++){
            if (nums[i] % 2 == 0 && nums[i] % 3 == 0){
                result += nums[i];
                count += 1;
            }
        }
        if (count != 0){
            return result/count;
        }
        return 0;
    }
}