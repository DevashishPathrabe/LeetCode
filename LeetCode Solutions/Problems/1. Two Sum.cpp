class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        int key;
        for (int i=0; i<nums.size(); i++){
            key = nums[i];
            if (umap.count(target - key) == 0){
                umap[key] = i;
            }
            else{
                return {umap[target-key], i};
            }
        }
        return {};
    }
};