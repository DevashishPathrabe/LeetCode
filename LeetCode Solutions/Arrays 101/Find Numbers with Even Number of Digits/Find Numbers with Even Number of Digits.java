class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int digit : nums){
            int numberOfDigits = 0;
            while (digit > 0){
                digit = digit / 10;
                numberOfDigits += 1;
            }
            if (numberOfDigits % 2 == 0){
                count += 1;
            }
        }
        return count;
    }
}