

int numberOfSteps (int num){
    int numberOfSteps = 0;
    while (num != 0){
        if (num%2 == 1){
            num--;
        } else{
            num /= 2;
        }
        numberOfSteps++;
    }
    return numberOfSteps;
}