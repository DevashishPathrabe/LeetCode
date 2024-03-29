class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> dq{0};
        for (int i=1; i<n; ++i){
            nums[i] = nums[dq.front()] + nums[i];
            while (!dq.empty() && nums[dq.back()] <= nums[i]){
                dq.pop_back();
            }
            dq.push_back(i);
            if (i-dq.front() >= k){
                dq.pop_front();
            }
        }
        return nums[n-1];
    }
};