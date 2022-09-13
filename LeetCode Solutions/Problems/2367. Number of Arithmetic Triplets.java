class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        int counter = 0;
        for (int i=0; i<nums.length-1; i++){
            int count = 0;
            int k = i;
            for (int j=i+1; j<nums.length; j++){
                if ((nums[j] - nums[k]) == diff) {
                    k = j;
                    count++;
                }
            }
            if (count > 1){
                counter++;
            }
        }
        return counter;
    }
}