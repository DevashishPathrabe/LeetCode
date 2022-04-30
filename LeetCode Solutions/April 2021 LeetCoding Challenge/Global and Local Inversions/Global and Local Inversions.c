

bool isIdealPermutation(int* A, int ASize){
    for (int i=0; i<ASize; i++){
        if (i-A[i] > 1 || i-A[i] < -1){
            return false;
        }
    }
    return true;
}