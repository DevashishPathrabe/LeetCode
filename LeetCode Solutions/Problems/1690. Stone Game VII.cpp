class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        vector<int> dpCurrent(stones.size()), dpLast(stones.size());
        for(int i=stones.size()-2; ~i; i--){
            int total = stones[i];
            dpLast.swap(dpCurrent);
            for(int j=i+1; j<stones.size(); j++){
                total += stones[j];
                dpCurrent[j] = max(total - stones[i] - dpLast[j], total - stones[j] - dpCurrent[j-1]);
            }
        }
        return dpCurrent[stones.size()-1];
    }
};