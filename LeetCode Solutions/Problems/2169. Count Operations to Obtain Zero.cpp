class Solution {
public:
    int countOperations(int num1, int num2) {
        int numberOfOperations = 0;
        while (num1 != 0 && num2 != 0){
            numberOfOperations += 1;
            if (num1 >= num2){
                num1 -= num2;
            }
            else{
                num2 -= num1;
            }
        }
        return numberOfOperations;
    }
};