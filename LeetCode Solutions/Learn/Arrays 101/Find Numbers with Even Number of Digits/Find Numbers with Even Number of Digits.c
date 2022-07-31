

int findNumbers(int* nums, int numsSize){
    int count = 0;
    for (int digit=0; digit<numsSize; digit++){
        int numberOfDigits = 0;
        while (nums[digit] > 0){
            nums[digit] /= 10;
            numberOfDigits++;
        }
        if (numberOfDigits % 2 == 0){
            count++;
        }
    }
    return count;
}