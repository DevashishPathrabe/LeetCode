class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        short[] nmap = new short[10001];
        int Sum = 0, maximumScore = 0;
        for (int left = 0, right = 0; right < nums.length; right++) {
            nmap[nums[right]]++;
            Sum += nums[right];
            while (nmap[nums[right]] > 1) {
                nmap[nums[left]]--;
                Sum -= nums[left++];
            }
            maximumScore = Math.max(maximumScore, Sum);
        }
        return maximumScore;
    }
}