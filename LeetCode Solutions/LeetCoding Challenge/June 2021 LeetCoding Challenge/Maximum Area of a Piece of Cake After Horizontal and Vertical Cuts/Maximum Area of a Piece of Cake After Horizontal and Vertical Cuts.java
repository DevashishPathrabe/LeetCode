class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        int maxHorizontalCuts = Math.max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length-1]),
            maxVerticalCuts = Math.max(verticalCuts[0], w - verticalCuts[verticalCuts.length-1]);
        for (int i=1; i<horizontalCuts.length; i++){
            maxHorizontalCuts = Math.max(maxHorizontalCuts, horizontalCuts[i] - horizontalCuts[i-1]);
        }
        for (int i=1; i<verticalCuts.length; i++){
            maxVerticalCuts = Math.max(maxVerticalCuts, verticalCuts[i] - verticalCuts[i-1]);
        }
        return (int)((long)maxHorizontalCuts * maxVerticalCuts % 1000000007);
    }
}