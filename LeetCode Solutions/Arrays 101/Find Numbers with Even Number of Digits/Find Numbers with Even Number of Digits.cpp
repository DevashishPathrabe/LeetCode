class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (int digit : nums){
            int numberOfDigits = 0;
            while (digit > 0){
                digit /= 10;
                numberOfDigits++;
            }
            if (numberOfDigits % 2 == 0){
                count++;
            }
        }
        return count;
    }
};