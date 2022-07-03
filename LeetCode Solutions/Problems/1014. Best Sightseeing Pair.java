class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int a = values[0], b = 0;
        for (int i=1; i<values.length; i++){
            b = Math.max(a + values[i] - i, b);
            a = Math.max(values[i] + i, a);
        }
        return b;
    }
}