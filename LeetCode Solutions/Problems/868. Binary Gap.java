class Solution {
    public int binaryGap(int n) {
        int longestDistance = 0, flag = 0, distance = 0;
        while (n != 0) {
            int t = n % 2;
            n /= 2;
            if (t == 1 && flag == 1) {
                distance++;
                longestDistance = Math.max(longestDistance, distance);
                distance = 0;
            } else if (t == 1 && flag == 0) {
                flag = 1;
            } else if (t == 0 && flag == 1) {
                distance++;
            }
        }
        return longestDistance;
    }
}