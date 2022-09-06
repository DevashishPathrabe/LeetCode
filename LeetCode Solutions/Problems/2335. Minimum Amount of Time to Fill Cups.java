class Solution {
    public int fillCups(int[] amount) {
        int maximum = 0, sum = 0;
        for(int a: amount) {
            maximum = Math.max(a, maximum);
            sum += a;
        }
        return Math.max(maximum, (sum + 1) / 2);
    }
}