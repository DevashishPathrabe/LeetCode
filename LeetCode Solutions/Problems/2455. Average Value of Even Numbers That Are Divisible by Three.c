int averageValue(int* nums, int numsSize){
    int result = 0, count = 0;
    for (int i=0; i<numsSize; i++){
        if (nums[i] % 2 == 0 && nums[i] % 3 == 0){
            result += nums[i];
            count += 1;
        }
    }
    if (count != 0){
        return result/count;
    }
    return 0;
}