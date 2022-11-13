class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0, i = 0, j = height.length - 1;
        while(i < j){
            maxArea = Math.max(maxArea, Math.min(height[i], height[j]) * (j-i));
            if(height[i] < height[j]){
                i += 1;
            }
            else{
                j -= 1;
            }
        }
        return maxArea;
    }
}