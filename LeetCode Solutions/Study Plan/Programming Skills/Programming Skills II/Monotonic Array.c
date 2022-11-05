

bool isMonotonic(int* nums, int numsSize){
    bool increasing = false, decreasing = false;
    for (int i=0; i<numsSize-1; i++){
        if (nums[i+1] > nums[i]){
            increasing = true;
        }
        if (nums[i+1] < nums[i]){
            decreasing = true;
        }
        if (increasing == true && decreasing == true){
            return false;
        }
    }
    return true;
}