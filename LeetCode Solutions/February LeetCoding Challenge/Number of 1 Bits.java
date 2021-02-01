public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int numberOf1bits = 0;
        while(n != 0) {
            numberOf1bits += n&1;
            n = n>>>1;
        }
        return numberOf1bits;
    }
}