class Solution {
    public int trailingZeroes(int n) {
        int zeroes = 0;
        while (n > 4){
            zeroes += n/5;
            n /= 5;
        }
        return zeroes;
    }
}