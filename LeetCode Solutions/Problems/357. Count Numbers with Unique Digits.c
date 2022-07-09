

int countNumbersWithUniqueDigits(int n){
    int result = 1, k = 9, m = 9;
    for (int i=0; i<n; i++){
        result += m;
        m *= (k - i);
    }
    return result;
}