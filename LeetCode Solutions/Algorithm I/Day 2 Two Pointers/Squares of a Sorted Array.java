class Solution {
    public int[] sortedSquares(int[] nums) {
        for(int number=0; number<nums.length; number++){
            nums[number] = nums[number] * nums[number];
        }
        Arrays.sort(nums);
        return nums;
    }
}