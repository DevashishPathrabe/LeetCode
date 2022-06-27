class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](auto& a, auto& b) { return b[1] < a[1];});
        int maxNumberOfUnits = 0;
        for (auto& b : boxTypes){
            int count = min(b[0], truckSize);
            maxNumberOfUnits += count * b[1], truckSize -= count;
			if (!truckSize){
                return maxNumberOfUnits;
            }
        }
        return maxNumberOfUnits;
    }
};