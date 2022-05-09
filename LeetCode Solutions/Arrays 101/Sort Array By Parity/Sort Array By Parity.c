

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* A, int ASize, int* returnSize){
    int left = 0, right = ASize - 1, temp;
    while (left < right){
        if (&A[left] % 2 == 1){
            temp = &A[left];
            &A[left] = &A[right];
            &A[right] = temp;
            right--;
        } else{
            left++;
        }
    }
    return A;
}