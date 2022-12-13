class Solution {
public:
    int pivotInteger(int n) {
        int sum = n * (n+1)/2, val = sqrt(sum); 
        return val*val == sum ? val : -1;
    }
};