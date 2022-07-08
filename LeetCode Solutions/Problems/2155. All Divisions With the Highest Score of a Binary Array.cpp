class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int currentScore = accumulate(nums.begin(), nums.end(), 0);
        int currentMax = currentScore;
        vector<int> result{0};
        for (int i=1; i<=nums.size(); ++i){
            currentScore += 1 - 2 * nums[i - 1];
            if (currentScore > currentMax){
                currentMax = currentScore;
                result = {i};
            } else if (currentScore == currentMax){
                result.emplace_back(i);
            }
        }
        return result;
    }
};