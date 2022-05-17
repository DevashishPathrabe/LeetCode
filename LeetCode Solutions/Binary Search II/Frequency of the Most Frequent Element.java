class Solution {
    public int maxFrequency(int[] nums, int k) {
        int result = 1, l = 0, r;
        long sum = 0;
        Arrays.sort(nums);
        for (r=0; r<nums.length; ++r) {
            sum += nums[r];
            while (sum + k < (long)nums[r] * (r - l + 1)) {
                sum -= nums[l];
                l += 1;
            }
            result = Math.max(result, r - l + 1);
        }
        return result;
    }
}