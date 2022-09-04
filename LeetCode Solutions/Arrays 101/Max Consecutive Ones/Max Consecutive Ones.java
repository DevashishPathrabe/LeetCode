class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int countOfOne = 0, maximumCountOfOne = 0;
        for (int digit : nums){
            if (digit == 1){
                countOfOne += 1;
                maximumCountOfOne = Math.max(maximumCountOfOne, countOfOne);
            } else{
                countOfOne = 0;
            }
        }
        return maximumCountOfOne;
    }
}