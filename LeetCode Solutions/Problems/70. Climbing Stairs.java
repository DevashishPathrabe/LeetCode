class Solution {
    public int climbStairs(int n) {
        int num = 0;
        int num1 = 1;
        for(int i=0; i<n; i++){
            int num2 = num + num1;
            num = num1;
            num1 = num2;
        }
        return(num1);
    }
}