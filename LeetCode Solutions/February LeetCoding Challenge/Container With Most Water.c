

int maxArea(int* height, int heightSize){
    int maxArea = 0, i = 0, j = heightSize - 1;
    while(i < j){
        maxArea = fmax(maxArea, fmin(height[i], height[j]) * (j-i));
        if(height[i] < height[j]){
            i += 1;
        }
        else{
            j -= 1;
        }
    }
    return maxArea;
}