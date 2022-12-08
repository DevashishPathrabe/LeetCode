class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());
        int maxHorizontalCuts = max(horizontalCuts[0], h - horizontalCuts.back()),
            maxVerticalCuts = max(verticalCuts[0], w - verticalCuts.back());
        for (int i=1; i<horizontalCuts.size(); i++){
            maxHorizontalCuts = max(maxHorizontalCuts, horizontalCuts[i] - horizontalCuts[i-1]);
        }
        for (int i=1; i<verticalCuts.size(); i++){
            maxVerticalCuts = max(maxVerticalCuts, verticalCuts[i] - verticalCuts[i-1]);
        }
        return (int)((long)maxHorizontalCuts * maxVerticalCuts % 1000000007);
    }
};