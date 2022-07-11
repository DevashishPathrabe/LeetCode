

bool isIdealPermutation(int* nums, int numsSize){
    for(int i=0; i<numsSize; i++){
        if(i-nums[i] > 1 || i-nums[i] < -1){
            return false;
        }
    }
    return true;
}