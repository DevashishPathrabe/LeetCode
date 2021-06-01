class Solution {
    public int maximumGap(int[] nums) {
        if(nums.length <= 1){
            return 0;
        }
        Arrays.sort(nums);
        int maximumDifference = 0;
        for(int num=1; num<nums.length; num++){
            maximumDifference = Math.max(maximumDifference, nums[num]-nums[num - 1]);
        }
        return maximumDifference;
    }
}