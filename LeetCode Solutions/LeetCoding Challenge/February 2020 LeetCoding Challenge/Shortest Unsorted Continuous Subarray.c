

int findUnsortedSubarray(int* nums, int numsSize){
    int lenNums = numsSize-1, left = -1, right = -1, maxNums = nums[0], minNums = nums[numsSize - 1];
    for(int i=0; i<numsSize; i++){
        int a = nums[i], b = nums[lenNums - i];
        if(a < maxNums){
            right = i;
        } else{
            maxNums = a;
        }
        if(b > minNums){
            left = i;
        } else{
            minNums = b;
        }
    }
    return fmax(0, left + right - lenNums + 1);
}