class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int numberOfOperations = 0, sum = 0, i = 0, j = nums.length-1;
        while(i<j){
            if(nums[i] + nums[j] == k){
                i++;
                j--;
                numberOfOperations++;
            }
            else if(nums[i] + nums[j] < k){
                i++;
            } else{
                j--;
            }
        }
        return numberOfOperations;
    }
}