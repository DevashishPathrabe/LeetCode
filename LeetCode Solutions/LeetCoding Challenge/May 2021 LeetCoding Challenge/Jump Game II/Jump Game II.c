

int jump(int* nums, int numsSize){
    int numsLength = numsSize - 1, current = -1, next = 0, result = 0;
    for (int i=0; next<numsLength; i++){
        if (i > current){
            result++,
            current = next;
        }
        next = fmax(next, nums[i] + i);
    };
    return result;
}