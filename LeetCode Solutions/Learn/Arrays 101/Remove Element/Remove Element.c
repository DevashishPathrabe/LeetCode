

int removeElement(int* nums, int numsSize, int val){
    int begin = 0, end = numsSize - 1;
    while (begin <= end){
        if (nums[begin] == val){
            nums[begin] = nums[end];
            nums[end] = nums[begin];
            end--;
        } else{
            begin++;
        }
    }
    return begin;
}