

int smallestRepunitDivByK(int k){
    if(k % 2 == 0 || k % 5 == 0){
        return -1;
    }
    int r = 0;
    for(int N=1; N<k+1; N++){
        r = (r * 10 + 1) % k;
        if(r == 0){
            return N;
        }
    }
    return 0;
}