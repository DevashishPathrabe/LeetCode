

int longestMountain(int* A, int ASize){
    int left = 0;
    int right = 1;
    int length = 0;
    while(right < ASize){
        if(A[left] >= A[right]){
            left += 1;
            right += 1;
        } else{
            int haveRight = 0;
            while(right < (ASize-1) && A[right] < A[right+1]){
                right += 1;
            }
            while(right < (ASize-1) && A[right] > A[right+1]){
                right += 1;
                haveRight = 1;
            }
            if(haveRight != 0){
                length = fmax(length,right-left+1);
            }
            left = right;
            right = left + 1;
        }
    }
    return length;
}