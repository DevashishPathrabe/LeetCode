class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxHorizontalCuts, maxVerticalCuts = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(len(horizontalCuts)):
            maxHorizontalCuts = max(maxHorizontalCuts, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(len(verticalCuts)):
            maxVerticalCuts = max(maxVerticalCuts, verticalCuts[i] - verticalCuts[i-1])
        return (maxHorizontalCuts * maxVerticalCuts) % 1000000007