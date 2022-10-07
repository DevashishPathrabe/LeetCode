class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        char nmap[10001]{0};
        int Sum = 0, maximumScore = 0;
        for (int left = 0, right = 0; right < nums.size(); right++) {
            nmap[nums[right]]++, Sum += nums[right];
            while (nmap[nums[right]] > 1)
                nmap[nums[left]]--, Sum -= nums[left++];
            maximumScore = max(maximumScore, Sum);
        }
        return maximumScore;
    }
};