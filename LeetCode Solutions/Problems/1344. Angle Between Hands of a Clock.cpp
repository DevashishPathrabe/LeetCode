class Solution {
public:
    double angleClock(int hour, int minutes) {
        return min(abs((minutes/60.0 +hour%12)* 30 - minutes*6), 360-abs((minutes/60.0 +hour%12)* 30 - minutes*6));
    }
};