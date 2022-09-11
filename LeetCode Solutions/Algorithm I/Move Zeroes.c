

void moveZeroes(int* nums, int numsSize){
    int i = 0;
    for(int j=0; j<numsSize; j++){
        if(nums[j] != 0){
            nums[i] = nums[j];
            if(j != i){
                nums[j] = 0;
            }
            i++;
        }
    }
}