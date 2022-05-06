class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int countOfOne = 0, maximumCountOfOne = 0;
        for (int digit : nums){
            if (digit == 1){
                countOfOne++;
                maximumCountOfOne = max(maximumCountOfOne, countOfOne);
            } else{
                countOfOne = 0;
            }
        }
        return maximumCountOfOne;
    }
};