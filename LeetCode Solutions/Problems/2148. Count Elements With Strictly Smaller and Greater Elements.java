class Solution {
    public int countElements(int[] nums) {
        Arrays.sort(nums);
        int minimum = nums[0];
        int maximum = nums[nums.length - 1];
        int count = 0;
        for (int i=0; i<nums.length; i++){
            if (nums[i] > minimum && nums[i] < maximum){
                count += 1;
            }
        }
        return count;
    }
}