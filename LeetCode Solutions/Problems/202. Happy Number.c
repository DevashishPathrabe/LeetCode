

bool isHappy(int n){
    int i=0;
    while (n!=1 && i<50){
        int x = 0;
        while (n != 0){
            x += pow((n%10), 2);
            n /= 10;
            i++;
        }
        n = x;
    }
    return n == 1;
}