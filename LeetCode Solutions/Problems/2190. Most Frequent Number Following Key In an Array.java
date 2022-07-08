class Solution {
    public int mostFrequent(int[] nums, int key) {
        int[] freq = new int[1001];
        for (int i=0; i<nums.length-1; i++){
            if (nums[i] == key) {
                freq[nums[i+1]]++;
            }
        }
        int max = 0;
        int maxCount = 0;
        for (int i=0; i<1001; i++){
            if (freq[i] > maxCount) {
                max = i;
                maxCount = freq[i];
            }
        }
        
        return max;
    }
}