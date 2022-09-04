

bool validMountainArray(int* A, int ASize){
    if (ASize < 3){
        return false;
    }
    int i = 1;
    while ((i < ASize) && (A[i-1] < A[i])){
        i++;
    }
    if ((i == ASize) || (i == 1)){
        return false;
    }
    while ((i < ASize) && (A[i-1] > A[i])){
        i++;
    }
    return ASize == i;
}