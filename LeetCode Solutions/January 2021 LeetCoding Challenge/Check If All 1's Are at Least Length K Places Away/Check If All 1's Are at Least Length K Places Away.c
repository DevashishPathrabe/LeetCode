

bool kLengthApart(int* nums, int numsSize, int k){
    for (int i=0, count=0; i<numsSize; i++){
        if (nums[i] == 1 && count < k && i != 0){
            return false;
        }
        else if (nums[i] == 1){
            count = 0;
        } else{
            count++;
        }
    }
    return true;
}