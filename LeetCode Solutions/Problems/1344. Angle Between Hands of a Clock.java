class Solution {
    public double angleClock(int hour, int minutes) {
        double hourDegree = (hour % 12) * 30;
        double minDegree = (minutes % 60) * 6;
        hourDegree += minDegree / 360 * 30;
        double angle = Math.abs(hourDegree - minDegree);
        return Math.min(360 - angle, angle);
    }
}