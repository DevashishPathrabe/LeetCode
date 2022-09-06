class Solution {
    public int[] numberOfPairs(int[] nums) {
        int []result = new int [2];
        int [] temp = new int[101];
        for (int i:nums){
            temp[i]++;
        }
        int count = 0;
        for (int i=0; i<101; i++){
            if (temp[i] % 2 != 0){
                count++;
            }
        }
        result[0] = (nums.length-count)/2;
        result[1] = count;
       return result;
    }
}