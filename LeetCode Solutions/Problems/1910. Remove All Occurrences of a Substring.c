

int countPairs(int* nums, int numsSize, int k){
    int n = numsSize;
    int count = 0;
    for (int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            if (nums[i] == nums[j] && (i*j)%k == 0){
                count += 1;
            }
        }
    }
    return count;
}