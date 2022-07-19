

int brokenCalc(int X, int Y){
    int result = 0;
    while(X < Y){
        result++;
        if(Y%2 > 0){
            Y++;
        } else{
            Y /= 2;
        }
    }
    return result + X - Y;
}