

int smallestRangeI(int* nums, int numsSize, int k){
    int length = numsSize;
    int minimum, maximum;
    minimum = maximum = nums[0];
    for (int i=1; i<length; i++){
        if (nums[i] > maximum){
            maximum = nums[i];
        }
        else if (nums[i] < minimum){
            minimum = nums[i];
        }
    }
    minimum += fmin(maximum - minimum, k);
    maximum -= fmin(maximum - minimum, k);
    return maximum - minimum;
}