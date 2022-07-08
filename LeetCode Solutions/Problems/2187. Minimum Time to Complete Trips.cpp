class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        auto f = [&](long long x){
        long long sum = 0;
        for (int t: time){
            sum += x / t;
        }
        return sum >= totalTrips;
    };
    long long low = 1, high = (long long)totalTrips * *min_element(time.begin(), time.end());
    while (low < high) {
        long long mid = low + (high - low) / 2;
        if (!f(mid)){
            low = mid + 1;
        }
        else{
            high = mid;
        }
    }
    return low;
    }
};