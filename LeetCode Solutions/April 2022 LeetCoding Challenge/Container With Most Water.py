class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea, i, j = 0, 0, len(height) - 1
        while(i < j):
            maximumArea = max(maximumArea, min(height[i], height[j]) * (j - i))
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return maximumArea