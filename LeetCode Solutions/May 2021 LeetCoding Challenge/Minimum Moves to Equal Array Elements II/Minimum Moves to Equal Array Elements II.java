class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int minimumNumberOfMoves = 0, median = nums[~~(nums.length / 2)];
        for(int num : nums){
            minimumNumberOfMoves += Math.abs(median - num);
        }
        return minimumNumberOfMoves;
    }
}