

int brokenCalc(int startValue, int target){
    int result = 0;
    while(startValue < target){
        result++;
        if(target % 2 > 0){
            target++;
        } else{
            target /= 2;
        }
    }
    return result + startValue - target;
}