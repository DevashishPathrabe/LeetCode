

int partitionDisjoint(int* nums, int numsSize){
    int max = nums[0];
    for(int i=0; i<numsSize-1; i++){
        int flag=1;
        if(nums[i] > max){
            max = nums[i];
        }
        for(int j=i+1; j<numsSize; j++){
            if(nums[j] < max){
                flag = 0;
                break;
            }
        }
        if(flag == 1){
            return i+1;
        }
    }
    return 0;
}