class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long low = 1, high = 100000000000000L;
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (!helper(mid, totalTrips, time)){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        return low;
    }
    private boolean helper(long x, int totalTrips, int[] time) {
        long sum = 0;
        for (int t: time){
            sum += x / t;
        }
        return sum >= totalTrips;
    }
}