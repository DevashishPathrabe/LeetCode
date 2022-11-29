

int maxTurbulenceSize(int* arr, int arrSize){
    int increment = 1, decrement = 1, result = 1;
    for (int i=1; i<arrSize; i++){
        if (arr[i] < arr[i-1]){
            decrement = increment + 1;
            increment = 1;
        }
        else if (arr[i] > arr[i-1]){
            increment = decrement + 1;
            decrement = 1;
        }
        else{
            increment = 1;
            decrement = 1;
        }
        result = fmax(result, fmax(increment, decrement));
    }
    return result;
}