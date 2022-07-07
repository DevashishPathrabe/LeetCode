

int trailingZeroes(int n){
    int zeroes=0;
    while(n > 4){
        zeroes += n/5;
        n = n/5;
    }
    return zeroes;
}