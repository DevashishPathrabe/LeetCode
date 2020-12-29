class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        water = 0
        if(len(height) < 3):
            return 0;
        leftMax, rightMax = height[0], height[len(height)-1]
        while(i <= j):
            leftMax, rightMax = max(leftMax, height[i]), max(rightMax, height[j])
            if(leftMax <= rightMax):
                water += leftMax-height[i]
                i+=1
            else:
                water += rightMax-height[j]
                j-=1
        return water