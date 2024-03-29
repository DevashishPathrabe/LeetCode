class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0, i = 0, j = height.size() - 1;
        while (i < j){
            maxArea = max(maxArea, min(height[i], height[j]) * (j-i));
            if (height[i] < height[j]){
                i += 1;
            }
            else{
                j -= 1;
            }
        }
        return maxArea;
    }
};